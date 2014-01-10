%{?_javapackages_macros:%_javapackages_macros}
%global artifactId javax.el

Name:           glassfish-el
Version:        2.2.5
Release:        5.0%{?dist}
Summary:        J2EE Expression Language Implementation
License:        CDDL or GPLv2 with exceptions
URL:            http://uel.java.net
# svn export https://svn.java.net/svn/uel~svn/tags/javax.el-2.2.5/ javax.el-2.2.5
# tar cvJf javax.el-2.2.5.tar.xz javax.el-2.2.5/
Source0:        %{artifactId}-%{version}.tar.xz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# glassfish-ha-api package don't include the license file
Source1:        glassfish-LICENSE.txt
BuildArch:      noarch

BuildRequires:  jvnet-parent
BuildRequires:  maven-local
BuildRequires:  maven-source-plugin
BuildRequires:  mvn(javax.el:javax.el-api)

%description
This project provides an implementation of the Expression Language (EL).
The main goals are:
 * Improves current implementation: bug fixes and performance improvements
 * Provides API for use by other tools, such as Netbeans

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{artifactId}-%{version}

cp -p %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt
%mvn_file :%{artifactId} %{name}
%mvn_alias :%{artifactId} "org.eclipse.jetty.orbit:com.sun.el"

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Aug 12 2013 Alexander Kurtakov <akurtako@redhat.com> 2.2.5-5
- Move xmvn customizations to prep.

* Wed Aug 07 2013 gil cattaneo <puntogil@libero.it> 2.2.5-4
- switch to XMvn, fix for rhbz#992384
- install license file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.5-2
- Add depmap for org.eclipse.jetty.orbit
- Resolves: rhbz#918514

* Fri Feb 1 2013 David Xie <david.scriptfan@gmail.com> - 2.2.5-1
- Initial version of package
