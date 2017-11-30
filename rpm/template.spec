Name:           ros-kinetic-qb-device-srvs
Version:        1.2.2
Release:        0%{?dist}
Summary:        ROS qb_device_srvs package

Group:          Development/Libraries
License:        BSD 3-Clause
URL:            http://wiki.ros.org/qb_device_srvs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-qb-device-msgs
Requires:       ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-qb-device-msgs
BuildRequires:  ros-kinetic-std-srvs

%description
This package contains the device-independent custom ROS services for qbrobotics®
devices.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Nov 30 2017 Alessandro Tondo <alessandro.tondo@qbrobotics.com> - 1.2.2-0
- Autogenerated by Bloom

* Fri Nov 24 2017 Alessandro Tondo <alessandro.tondo@qbrobotics.com> - 1.1.0-0
- Autogenerated by Bloom

* Tue Jun 27 2017 Alessandro Tondo <alessandro.tondo@qbrobotics.com> - 1.0.8-0
- Autogenerated by Bloom

* Mon Jun 26 2017 Alessandro Tondo <alessandro.tondo@qbrobotics.com> - 1.0.7-0
- Autogenerated by Bloom

* Fri Jun 23 2017 Alessandro Tondo <alessandro.tondo@qbrobotics.com> - 1.0.6-0
- Autogenerated by Bloom

* Mon Jun 19 2017 Alessandro Tondo <alessandro.tondo@qbrobotics.com> - 1.0.1-0
- Autogenerated by Bloom

