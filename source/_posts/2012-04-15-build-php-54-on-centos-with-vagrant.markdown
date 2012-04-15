---
layout: post
title: "Build PHP 5.4 on CentOS with Vagrant" 
author: Chris Hartjes
date: 2012-04-15
comments: true 
sharing: true 
---
I like the idea of using [Vagrant](http://vagrantup.com) to create virtual
machines for my development work. Doing things this way I think keeps the
host machine cleaner and allows you the ability to distribute those VM's
to other people as well.

My old boss Ben Ramsey did a very informative post on [getting PHP 5.4 configured on CentOS](http://benramsey.com/blog/2012/03/build-php-54-on-centos-62/)
so I decided to one-up him by taking his instructions and creating a [Puppet](http://puppetlabs.com/)
manifest so you could do this using Vagrant or on any server that you can 
provision using Puppet.

First, you will need a CentOS base box to play with. I used [this box](http://www.vagrantbox.es/37/)
but I think any CentOS 6.0 (or above) base box will do. If you are feeling really
adventurous you could grab an ISO and use [Vewee](https://github.com/jedi4ever/veewee) 
and follow [these instructions](http://www.ducea.com/2011/08/15/building-vagrant-boxes-with-veewee/)
to create your own. 

Whatever box you choose, the next step is to create the directory where your VM
will run and run 'vagrant init' with the name of the box and then edit the Vagrantfile.
Here's a condensed version of my Vagrantfile

{% codeblock lang:ruby %}
Vagrant::Config.run do |config|
  config.vm.box = "centos-60-x86_64"
    
  config.vm.forward_port 80, 8080
  config.vm.forward_port 8000, 8000
  
  config.vm.provision :puppet do |puppet|
     puppet.manifests_path = "manifests"
     puppet.manifest_file  = "default.pp"
  end
end
{% endcodeblock %}

Those port forwards are identical to the ones that Ben suggested using. You
can get rid of the one that maps port 8000 if you don't feel like playing
around with the new built-in web server introducted in PHP 5.4.

Now, create the manifests directory inside the directory where you are placing
the new VM and add a file called default.pp that looks like this:

{% codeblock lang:ruby %}
# Puppet manifest for a PHP 5.4 dev machine

class httpd {

  package { "httpd":
    ensure => present,
  }

  package { "httpd-devel":
    ensure  => present,
    require => Package["httpd"]
  }

  exec {
    "/bin/sed -i '/22/ i -A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT' /etc/sysconfig/iptables":
      alias   => "open-port80",
      require => Package["httpd-devel"],
  }

  exec {
    "/bin/sed -i '/22/ i -A INPUT -m state --state NEW -m tcp -p tcp --dport 8000 -j ACCEPT' /etc/sysconfig/iptables":
      alias   => "open-port8000",
      require => Package["open-port80"],
  }
  
  exec {
    "/etc/init.d/iptables restart",
      alias   => "restart-iptables",
      require => Package["open-port8000"],
  }
}

class phpdev {
  package { "libxml2-devel":
    ensure  => present,
    require => Package["httpd-devel"]
  }

  package { "libXpm-devel":
    ensure  => present,
    require => Package["libxml2-devel"]
  }
 
  package { "gmp-devel":
    ensure  => present,
    require => Package["libXpm-devel"]
  }
 
  package { "libicu-devel":
    ensure  => present,
    require => Package["gmp-devel"]
  }

  package { "t1lib-devel":
    ensure  => present,
    require => Package["libicu-devel"]
  }
  
  package { "aspell-devel":
    ensure  => present,
    require => Package["t1lib-devel"]
  }
  
  package { "openssl-devel":
    ensure  => present,
    require => Package["aspell-devel"]
  }
 
  package { "bzip2-devel":
    ensure  => present,
    require => Package["openssl-devel"]
  }
 
  package { "libcurl-devel":
    ensure  => present,
    require => Package["bzip2-devel"]
  }

  package { "libjpeg-devel":
    ensure  => present,
    require => Package["libcurl-devel"]
  }

  package { "libvpx-devel":
    ensure  => present,
    require => Package["libjpeg-devel"]
  }

  package { "libpng-devel":
    ensure  => present,
    require => Package["libvpx-devel"]
  }

  package { "freetype-devel":
    ensure  => present,
    require => Package["libpng-devel"]
  }

  package { "readline-devel":
    ensure  => present,
    require => Package["freetype-devel"]
  }

  package { "libtidy-devel":
    ensure  => present,
    require => Package["readline-devel"]
  }

  package { "libxslt-devel":
    ensure  => present,
    require => Package["libtidy-devel"]
  }
}

class rpmforge {
  exec {
    "/usr/bin/wget http://packages.sw.be/rpmforge-release/rpmforge-release-0.5.2-2.el6.rf.x86_64.rpm":
      alias   => "grab-rpmforge",
      require => Package["libxslt-devel"],
  }

  exec {
    "/bin/rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt":
      alias   => "import-key",
      require => Exec["grab-rpmforge"],
  }

  exec {
    "/bin/rpm -i rpmforge-release-0.5.2-2.el6.rf.*.rpm":
      alias   => "install-rpmforge",
      require => Exec["import-key"],
  }

  package { "libmcrypt-devel":
    ensure  => present,
    require => Exec["install-rpmforge"]
  }
}

include httpd
include phpdev
include rpmforge
{% endcodeblock %}

Now, there *appears* to be a lot of stuff going on in there, but it's actually
quite simple. I broke things down into 3 distinct groups. 

The first group (
which I called 'httpd') makes sure that we install Apache 2 and the development
libraries and header files that will be needed to compile PHP. Then we open up
the firewall to allow access to the VM on those two ports. By default Vagrant
maps port 22 on the VM to port 2222 on the VM, so no need to add that in. 

The next group (phpdev) is installing all the support libraries that Ben recommended 
in his own article.

Finally we need to execute a few commands to allows us to also install libmcrypt-devel
because it is not part of the standard CentOS distribution, but is available via
RPMForge.

Save that file (make sure there are no typos either from me or from you!), then type
'vagrant up' and it will try and it will try to provision your new server with this
Puppet manifest and add in all your files.

Then you can follow the rest of Ben's instructions on how to compile PHP 5.4 (I
installed PHP 5.4.1RC1 just to be living on the edge) and don't forget to verify
that your Apache setup is configured to all you to serve up PHP files.

I think that you can have a cutting-edge CentOS VM with the latest PHP installed on
it up and running in under an hour from starting to download your CentOS Vagrant
base box to verifying your test file with phpinfo() in it worked. 

