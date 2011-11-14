%global with_doc %{!?_without_doc:1}%{?_without_doc:0}

Name:             openstack-nova
Version:          2011.3
Release:          7%{?dist}
Summary:          OpenStack Compute (nova)

Group:            Applications/System
License:          ASL 2.0
URL:              http://openstack.org/projects/compute/
Source0:          http://launchpad.net/nova/diablo/2011.3/+download/nova-%{version}.tar.gz
Source1:          nova.conf
Source6:          nova.logrotate

Source11:         openstack-nova-api.service
Source12:         openstack-nova-compute.service
Source13:         openstack-nova-network.service
Source14:         openstack-nova-objectstore.service
Source15:         openstack-nova-scheduler.service
Source16:         openstack-nova-volume.service
Source17:         openstack-nova-direct-api.service
Source18:         openstack-nova-ajax-console-proxy.service
Source19:         openstack-nova-vncproxy.service

Source20:         nova-sudoers
Source21:         nova-polkit.pkla
Source22:         nova-ifc-template

#
# Patches managed here: https://github.com/markmc/nova/tree/fedora-patches
#
#   $> git format-patch b0e855e
#   $> for p in 00*.patch; do echo "Patch${p:2:2}:          $p"; done
#   $> for p in 00*.patch; do echo "%patch${p:2:2} -p1"; done
#
Patch01:          0001-Add-tools-rfc.sh-from-master.patch
Patch02:          0002-Don-t-use-GitPython-for-authors-check.patch
Patch03:          0003-Made-jenkins-email-pruning-more-resilient.patch
Patch04:          0004-Removing-old-code-that-snuck-back-in.patch
Patch05:          0005-Fix-outstanding-pep8-errors-for-a-clean-trunk.patch
Patch06:          0006-Point-tools-rfc.sh-at-the-right-branch.patch
Patch07:          0007-Makes-sure-to-recreate-gateway-for-moved-ip.patch
Patch08:          0008-put-fully-qualified-domain-name-in-local-hostname.patch
Patch09:          0009-Fix-the-grantee-group-loading-for-source-groups.patch
Patch10:          0010-Call-endheaders-when-auth_token-is-None.-Fixes-bug-8.patch
Patch11:          0011-Removed-db_pool-complexities-from-nova.db.sqlalchemy.patch
Patch12:          0012-Raise-InsufficientFreeMemory.patch
Patch13:          0013-Don-t-leak-exceptions-out-to-users.patch
Patch14:          0014-Makes-snapshots-work-for-amis.-Fixes-bug-873156.patch
Patch15:          0015-Add-missing-author.patch
Patch16:          0016-Make-snapshots-private-by-default.patch
Patch17:          0017-Snapshots-backups-can-no-longer-happen-simultaneousl.patch
Patch18:          0018-Fixed-bug-lp850602.patch
Patch19:          0019-bug-861310.patch
Patch20:          0020-Enforce-snapshot-cleanup.patch
Patch21:          0021-bug-lp845714.patch
Patch22:          0022-Added-1.0.4-version-specifier-to-kombu-in-pip-requir.patch
Patch23:          0023-Adds-the-tenant-id-to-the-create-images-response-Loc.patch
Patch24:          0024-Fixes-bug-862633-OS-api-consoles-create-broken.patch
Patch25:          0025-Deallocate-ip-if-build-fails.patch
Patch26:          0026-Stop-returning-correct-password-on-api-calls.patch
Patch27:          0027-Handle-pidfile-exception-for-dnsmasq.patch
Patch28:          0028-Make-sure-unknown-extensions-return-404.patch
Patch29:          0029-Include-original-exception-in-ClassNotFound-exceptio.patch
Patch30:          0030-Ensure-non-default-FLAGS.logfile_mode-is-properly-co.patch
Patch31:          0031-Explicit-errors-on-confirm-revertResize-failures.patch
Patch32:          0032-Adds-ext4-and-reiserfs-to-_mount_filesystem.patch
Patch33:          0033-Improve-access-check-on-images.patch
Patch34:          0034-Fixes-bug-834633-Auto-assigning-floating-IPs.patch
Patch35:          0035-fixes-bug-883233.patch
Patch36:          0036-Add-INPUT-chain-rule-for-EC2-metadata-requests-lp-85.patch
Patch37:          0037-Have-nova-api-add-the-INPUT-rule-for-EC2-metadata-lp.patch
Patch38:          0038-Allow-the-user-to-choose-either-ietadm-or-tgtadm-lp-.patch
Patch39:          0039-Remove-VolumeDriver.sync_exec-method-lp-819997.patch
Patch40:          0040-Refactor-ietadm-tgtadm-calls-out-into-helper-classes.patch

BuildArch:        noarch
BuildRequires:    intltool
BuildRequires:    python-setuptools
BuildRequires:    python-distutils-extra >= 2.18
BuildRequires:    python-netaddr
BuildRequires:    python-lockfile

Requires:         python-nova = %{version}-%{release}
Requires:         openstack-glance

Requires:         python-paste
Requires:         python-paste-deploy

Requires:         libvirt-python
Requires:         libvirt >= 0.8.2
Requires:         libxml2-python
Requires:         python-cheetah
Requires:         MySQL-python

Requires:         euca2ools
Requires:         openssl
Requires:         rabbitmq-server
Requires:         sudo

Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
Requires(pre):    shadow-utils qemu-kvm

%description
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

%package -n       python-nova
Summary:          Nova Python libraries
Group:            Applications/System

Requires:         vconfig
Requires:         PyXML
Requires:         curl
Requires:         m2crypto
Requires:         libvirt-python
Requires:         python-anyjson
Requires:         python-IPy
Requires:         python-boto
Requires:         python-kombu
Requires:         python-amqplib
Requires:         python-daemon
Requires:         python-eventlet
Requires:         python-greenlet
Requires:         python-gflags
Requires:         python-lockfile
Requires:         python-lxml
Requires:         python-mox
Requires:         python-redis
Requires:         python-routes
Requires:         python-sqlalchemy
Requires:         python-tornado
Requires:         python-twisted-core
Requires:         python-twisted-web
Requires:         python-webob
Requires:         python-netaddr
Requires:         python-glance
Requires:         python-novaclient
Requires:         python-paste-deploy
Requires:         python-migrate
Requires:         python-ldap
Requires:         radvd
Requires:         iptables iptables-ipv6
Requires:         iscsi-initiator-utils
Requires:         scsi-target-utils
Requires:         lvm2
Requires:         socat
Requires:         coreutils

%description -n   python-nova
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Compute
Group:            Documentation

Requires:         %{name} = %{version}-%{release}

BuildRequires:    systemd-units
BuildRequires:    python-sphinx
BuildRequires:    graphviz
BuildRequires:    python-distutils-extra

BuildRequires:    python-nose
# Required to build module documents
BuildRequires:    python-IPy
BuildRequires:    python-boto
BuildRequires:    python-eventlet
BuildRequires:    python-gflags
BuildRequires:    python-routes
BuildRequires:    python-sqlalchemy
BuildRequires:    python-tornado
BuildRequires:    python-twisted-core
BuildRequires:    python-twisted-web
BuildRequires:    python-webob
# while not strictly required, quiets the build down when building docs.
BuildRequires:    python-carrot, python-mox, python-suds, m2crypto, bpython, python-memcached, python-migrate

%description      doc
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains documentation files for nova.
%endif

%prep
%setup -q -n nova-%{version}

# Replicate screwup during git->bzr switch
%patch04 -p1 -R

# Now apply the patches from git
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
# Manually auto-generate to work around sphinx-build segfault
./generate_autodoc_index.sh
SPHINX_DEBUG=1 sphinx-build -b man source build/man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 build/man/*.1 %{buildroot}%{_mandir}/man1/

%if 0%{?with_doc}
SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo
%endif
popd

# Give stack, instance-usage-audit and clear_rabbit_queues a reasonable prefix
mv %{buildroot}%{_bindir}/stack %{buildroot}%{_bindir}/nova-stack
mv %{buildroot}%{_bindir}/instance-usage-audit %{buildroot}%{_bindir}/nova-instance-usage-audit
mv %{buildroot}%{_bindir}/clear_rabbit_queues %{buildroot}%{_bindir}/nova-clear-rabbit-queues

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/buckets
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/images
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/tmp
install -d -m 755 %{buildroot}%{_localstatedir}/log/nova

# Setup ghost sqlite DB
touch %{buildroot}%{_sharedstatedir}/nova/nova.sqlite

# Setup ghost CA cert
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 755 nova/CA/*.sh %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 644 nova/CA/openssl.cnf.tmpl %{buildroot}%{_sharedstatedir}/nova/CA
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA/{certs,crl,newcerts,projects,reqs}
touch %{buildroot}%{_sharedstatedir}/nova/CA/{cacert.pem,crl.pem,index.txt,openssl.cnf,serial}
install -d -m 750 %{buildroot}%{_sharedstatedir}/nova/CA/private
touch %{buildroot}%{_sharedstatedir}/nova/CA/private/cakey.pem

# Install config file
install -d -m 755 %{buildroot}%{_sysconfdir}/nova
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_sysconfdir}/nova/nova.conf

# Install initscripts for Nova services
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_unitdir}/openstack-nova-api.service
install -p -D -m 755 %{SOURCE12} %{buildroot}%{_unitdir}/openstack-nova-compute.service
install -p -D -m 755 %{SOURCE13} %{buildroot}%{_unitdir}/openstack-nova-network.service
install -p -D -m 755 %{SOURCE14} %{buildroot}%{_unitdir}/openstack-nova-objectstore.service
install -p -D -m 755 %{SOURCE15} %{buildroot}%{_unitdir}/openstack-nova-scheduler.service
install -p -D -m 755 %{SOURCE16} %{buildroot}%{_unitdir}/openstack-nova-volume.service
install -p -D -m 755 %{SOURCE17} %{buildroot}%{_unitdir}/openstack-nova-direct-api.service
install -p -D -m 755 %{SOURCE18} %{buildroot}%{_unitdir}/openstack-nova-ajax-console-proxy.service
install -p -D -m 755 %{SOURCE19} %{buildroot}%{_unitdir}/openstack-nova-vncproxy.service

# Install sudoers
install -p -D -m 440 %{SOURCE20} %{buildroot}%{_sysconfdir}/sudoers.d/nova

# Install logrotate
install -p -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-nova

# Install pid directory
install -d -m 755 %{buildroot}%{_localstatedir}/run/nova

# Install template files
install -p -D -m 644 nova/auth/novarc.template %{buildroot}%{_datarootdir}/nova/novarc.template
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %{buildroot}%{_datarootdir}/nova/client.ovpn.template
install -p -D -m 644 nova/virt/libvirt.xml.template %{buildroot}%{_datarootdir}/nova/libvirt.xml.template
install -p -D -m 644 nova/virt/interfaces.template %{buildroot}%{_datarootdir}/nova/interfaces.template
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_datarootdir}/nova/interfaces.template

install -d -m 755 %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d
install -p -D -m 644 %{SOURCE21} %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

# Remove ajaxterm and various other tools
rm -fr %{buildroot}%{_datarootdir}/nova/{ajaxterm,euca-get-ajax-console,install_venv.py,nova-debug,pip-requires,clean-vlans,with_venv.sh,esx}

# Remove unneeded in production stuff
rm -fr %{buildroot}%{python_sitelib}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}/usr/share/doc/nova/README*

%pre
getent group nova >/dev/null || groupadd -r nova --gid 162
getent passwd nova >/dev/null || \
useradd --uid 162 -r -g nova -G nova,nobody,qemu -d %{_sharedstatedir}/nova -s /sbin/nologin \
-c "OpenStack Nova Daemons" nova
exit 0

%post
# Initialize the DB
if [ ! -f %{_sharedstatedir}/nova/nova.sqlite ]; then
    runuser -l -s /bin/bash -c 'nova-manage --flagfile=/dev/null --logdir=%{_localstatedir}/log/nova --state_path=%{_sharedstatedir}/nova db sync' nova
    chmod 600 %{_sharedstatedir}/nova/nova.sqlite
fi
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
if [ $1 -eq 0 ] ; then
    for svc in api compute network objectstore scheduler volume direct-api ajax-console-proxy vncproxy; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in api compute network objectstore scheduler volume direct-api ajax-console-proxy vncproxy; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi

%files
%doc LICENSE
%dir %{_sysconfdir}/nova
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/nova.conf
%config(noreplace) %{_sysconfdir}/nova/api-paste.ini
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-nova
%config(noreplace) %{_sysconfdir}/sudoers.d/nova
%config(noreplace) %{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

%dir %attr(0755, nova, root) %{_localstatedir}/log/nova
%dir %attr(0755, nova, root) %{_localstatedir}/run/nova

%{_bindir}/nova-*
%{_unitdir}/openstack-nova-*.service
%{_datarootdir}/nova
%{_mandir}/man1/nova*.1.gz

%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova
%dir %{_sharedstatedir}/nova/buckets
%dir %{_sharedstatedir}/nova/images
%dir %{_sharedstatedir}/nova/instances
%dir %{_sharedstatedir}/nova/keys
%dir %{_sharedstatedir}/nova/networks
%dir %{_sharedstatedir}/nova/tmp
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/nova.sqlite

%dir %{_sharedstatedir}/nova/CA/
%dir %{_sharedstatedir}/nova/CA/certs
%dir %{_sharedstatedir}/nova/CA/crl
%dir %{_sharedstatedir}/nova/CA/newcerts
%dir %{_sharedstatedir}/nova/CA/projects
%dir %{_sharedstatedir}/nova/CA/reqs
%{_sharedstatedir}/nova/CA/*.sh
%{_sharedstatedir}/nova/CA/openssl.cnf.tmpl
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/cacert.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/crl.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/index.txt
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/openssl.cnf
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/serial
%dir %attr(0750, -, -) %{_sharedstatedir}/nova/CA/private
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/private/cakey.pem

%files -n python-nova
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelib}/nova
%{python_sitelib}/nova-%{version}-*.egg-info

%if 0%{?with_doc}
%files doc
%doc LICENSE doc/build/html
%endif

%changelog
* Mon Nov 14 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-7
- Add ~20 significant fixes from upstream stable branch

* Wed Oct 26 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-6
- Fix password leak in EC2 API (#749385, CVE 2011-4076)

* Mon Oct 24 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-5
- Fix block migration (#741690)

* Mon Oct 17 2011 Bob Kukura <rkukura@redhat.com> - 2011.3-4
- Add dependency on python-amqplib (#746685)

* Wed Sep 28 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-3
- Fix lazy load exception with security groups (#741307)
- Fix issue with nova-network deleting the default route (#741686)
- Fix errors caused by MySQL connection pooling (#741312)

* Mon Sep 26 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-2
- Manage the package's patches in git; no functional changes.

* Thu Sep 22 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-1
- Update to Diablo final.
- Drop some upstreamed patches.
- Update the metadata-accept patch to what's proposed for essex.
- Switch rpc impl from carrot to kombu.

* Mon Sep 19 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.10.d4
- Use tgtadm instead of ietadm (#737046)

* Wed Sep 14 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.9.d4
- Remove python-libguestfs dependency (#738187)

* Mon Sep  5 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.8.d4
- Add iptables rule to allow EC2 metadata requests (#734347)

* Sat Sep  3 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.7.d4
- Add iptables rules to allow requests to dnsmasq (#734347)

* Wed Aug 31 2011 Angus Salkeld <asalkeld@redhat.com> - 2011.3-0.6.d4
- Add the one man page provided by nova.
- Start services with --flagfile rather than --flag-file (#735070)

* Tue Aug 30 2011 Angus Salkeld <asalkeld@redhat.com> - 2011.3-0.5.d4
- Switch from SysV init scripts to systemd units (#734345)

* Mon Aug 29 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.4.d4
- Don't generate root CA during %post (#707199)
- The nobody group shouldn't own files in /var/lib/nova
- Add workaround for sphinx-build segfault

* Fri Aug 26 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.3.d4
- Update to diablo-4 milestone
- Use statically assigned uid:gid 162:162 (#732442)
- Collapse all sub-packages into openstack-nova; w/o upgrade path
- Reduce use of macros
- Rename stack to nova-stack
- Fix openssl.cnf.tmpl script-without-shebang rpmlint warning
- Really remove ajaxterm
- Mark polkit file as %config

* Mon Aug 22 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.2.1449bzr
- Remove dependency on python-novaclient

* Wed Aug 17 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.1.1449bzr
- Update to latest upstream.
- nova-import-canonical-imagestore has been removed
- nova-clear-rabbit-queues was added

* Tue Aug  9 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.2.1409bzr
- Update to newer upstream
- nova-instancemonitor has been removed
- nova-instance-usage-audit added

* Tue Aug  9 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.1.bzr1130
- More cleanups
- Change release tag to reflect pre-release status

* Wed Jun 29 2011 Matt Domsch <mdomsch@fedoraproject.org> - 2011.3-1087.1
- Initial package from Alexander Sakhnov <asakhnov@mirantis.com>
  with cleanups by Matt Domsch
