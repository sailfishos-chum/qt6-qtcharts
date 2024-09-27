%global  qt_version 6.7.2

Summary: Qt6 - Charts component
Name:    qt6-qtcharts
Version: 6.7.2
Release: 0%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
Source0: %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: clang
BuildRequires: ninja
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{qt_version}
BuildRequires: pkgconfig(xkbcommon)

%description
Qt Charts module provides a set of easy to use chart components. It uses the Qt Graphics View Framework, therefore charts can be easily
integrated to modern user interfaces. Qt Charts can be used as QWidgets, QGraphicsWidget, or QML types.
Users can easily create impressive graphs by selecting one of the charts themes.

%package devel
Summary: Development files for %{name}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_qt6 \
    -DQT_BUILD_EXAMPLES:BOOL=OFF \
    -DQT_INSTALL_EXAMPLES_SOURCES=OFF

%cmake_build

%install
%cmake_install


%files
%license LICENSES/GPL*
%{_qt6_libdir}/libQt6Charts.so.6*
%{_qt6_libdir}/libQt6ChartsQml.so.6*
%{_qt6_qmldir}/QtCharts/

%files devel
%{_qt6_headerdir}/QtCharts/
%{_qt6_headerdir}/QtChartsQml/
%{_qt6_libdir}/libQt6Charts.so
%{_qt6_libdir}/libQt6Charts.prl
%{_qt6_libdir}/libQt6ChartsQml.so
%{_qt6_libdir}/libQt6ChartsQml.prl
%dir %{_qt6_libdir}/cmake/Qt6Charts/
%{_qt6_libdir}/cmake/Qt6Charts/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtChartsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml2*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ChartsQml/
%{_qt6_libdir}/cmake/Qt6ChartsQml/
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc
