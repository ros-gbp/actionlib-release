Name:           ros-jade-actionlib
Version:        1.11.3
Release:        0%{?dist}
Summary:        ROS actionlib package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/actionlib
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-jade-actionlib-msgs
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roscpp
Requires:       ros-jade-rospy
Requires:       ros-jade-rostest
Requires:       ros-jade-std-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-jade-actionlib-msgs
BuildRequires:  ros-jade-catkin >= 0.5.78
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rosnode
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-std-msgs

%description
The actionlib stack provides a standardized interface for interfacing with
preemptable tasks. Examples of this include moving the base to a target
location, performing a laser scan and returning the resulting point cloud,
detecting the handle of a door, etc.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Dec 31 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.11.3-0
- Autogenerated by Bloom

