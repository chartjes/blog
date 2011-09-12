--- 
layout: post
title: \"U R Doin It Wrong\" - Adventures with flexible forms in Zend Framework
---
<p><a href="http://framework.zend.com/manual/en/zend.form.html">Zend_Form</a> is a super-powerful, force-of-nature tool.  By force-of-nature I mean it does all this crazy stuff, and you can see it doing it, but I am not alone in admitting that taming it sometimes is very difficult.  When building tools to make form programatically you either severely limit peoples options or make it so flexible that there are multiple ways to get something done.  Given the concept that Zend Framework "treats you like an adult" (I cannot find the blog post where I read this) it is not surprising that Zend_Form takes the flexible route.
</p>
<p>
Before I go any further, thanks (again) to <a href="http://twitter.com/elazar">@elazar</a> and to <a href="http://akrabat.com/">Rob Allen</a> aka <a href="http://twitter.com/akrabat">@akrabat</a> for helping me solve this particular problem.
</p>
<p>
Okay, so onto my problem.  I was creating a page for a fantasy baseball draft application to process transaction requests.  You could do one thing, and one thing only:  make a request to add a free agent to your team and what player off your team you wanted to drop.  Since I needed to locate form elements in specific places in the layout, I didn't do the usual < ?= $form ?> in my template, instead I created a bunch of setX methods, with X representing a specific form element.  Then, in my templates I simply did < ?= $form->X ?> where X represents the specific element.  Let me show you what I mean:
</p>
{% codeblock lang:php %}
            <form action="/baseball/<?= $this->league ?>/transactions/process" method="post">
                < ?= $this->transactionForm->teamId ?>
                < ?= $this->transactionForm->shortLeagueName ?>
                <table width="100%">
                    <tr>
                        <th width="50%" align="center">Players on your Team</th>
                        <th width="50%" align="center">Players Available</th>
                    </tr>
                    <tr>
                        <td align="center" valign="top">
                            < ?= $this->transactionForm->players ?>
                        </td>
                        <td align="center" valign="top">
                            <div id="freeAgentList">
                                < ?= $this->transactionForm->freeAgents ?>
                            </div>
                        </td>
                    </tr>
                </table>
                <input type="submit" id="transactionFormSubmit" value="Request Selection"/>
            </form>
{% endcodeblock %}
<p>
I did this figuring it would give me lots of flexibility.  Then, the pain started.
</p>
<p>
I kept wondering why every time I validated the form, it kept coming back as true.  I had a requirement that to have a successful transaction request, they had to select both a player to drop from their own team AND a free agent to add.  I had put into the form validation that a free agent was required, but it never seemed to be triggered.  Off to <a href="http://stackoverflow.com">Stack Overflow</a> I went to ask for help, along with pleas for help on Twitter.  I had thought I was doing something subtly wrong, and I was right.
</p>
<p>
Here's the finished, working code.  I will explain what I had been doing wrong.  By the way, if you can think of a better way to do something of the more "hackish" stuff in there, I'd appreciate it.
</p>
<p>
{% codeblock lang:php %}
    public function indexAction()
    {
        $form = new Baseball_Form_Transactions();
        $options = array(
            'teamId' => $this->teamId,
            'position' => 'C',
            'leagueShortName' => $this->league,
            'status' => 0
        );

        $form->setMyPlayers($options);
        $form->setFreeAgents($options);
        $form->setTeamId($options);
        $form->setShortLeagueName($options);

        if ($this->getRequest()->isPost()) {
            // This is hack to make sure we pull back the list of free agents for
            // the player's position
            $postData = $this->_request->getPost();
            $player = Doctrine::getTable('Player')->find($postData['players']);
            $options['position'] = $player['position'];
            $form->setFreeAgents($options);

            if ($form->isValid($this->_request->getPost())) {
                $data = $form->getValues();
                $leagueInfo = Doctrine::getTable('League')->findOneByShortName($data['shortLeagueName'])->toArray();

                // Create the request top drop an existing player		
                $transactionInfo = array(
                    'league_id' => $leagueInfo['id'],
                    'team_id' => $data['teamId'],
                    'player_id' => $data['players'],
                    'type' => 'drop',
                    'target_team_id' => 0,
                    'transaction_date' => date('Y-m-d H:m:s'),
                    'shortLeagueName' => $data['shortLeagueName'],
                    'group_id' => uniqid()
                );
                $transaction = new Transaction();
                $transaction->fromArray($transactionInfo);
                $transaction->save();

                // Now we do the request to add a player
                $transactionInfo['team_id'] = 0;
                $transactionInfo['player_id'] = $data['freeAgents'];
                $transactionInfo['target_team_id'] = $data['teamId'];
                $transactionInfo['type'] = 'add';
                $transaction = new Transaction();
                $transaction->fromArray($transactionInfo);
                $transaction->save();
                $this->_flashMessenger->addMessage('Added transaction');
            }
        }

        $this->view->transactionForm = $form;
        $this->view->messages = $this->_flashMessenger->getMessages();
        $transaction = new Transaction();
        $this->view->transactions = $transaction->byTeam($options);
    }
{% endcodeblock %}
</p>
<p>The big mistake?  I was not setting up all the form elements via my setX calls BEFORE I did the validation.  Because I didn't, those elements didn't exist, and therefore the validation never got called.  See, I told you my mistake was (a) dumb and (b) subtle.
</p>
<p>
I think I did the right thing with my method of creating the form elements outside of the init() method to give me the ability to layout things where I wanted them.  I'm interested in finding out how other people have solved the same problem.
</p>
