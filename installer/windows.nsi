# This script will convert the pyinstaller bundle to a Windows installer
# makensis /DVERSION=0.10.50 installer\windows.nsi

!define MULTIUSER_EXECUTIONLEVEL Highest
!define MULTIUSER_MUI
!define MULTIUSER_INSTALLMODE_COMMANDLINE
!define MULTIUSER_INSTALLMODE_INSTDIR "Amulet Team\Amulet ${VERSION}"
!define MULTIUSER_USE_PROGRAMFILES64
!include MultiUser.nsh

!include "MUI2.nsh"
!define MUI_ICON "logo.ico"
!define MUI_UNICON "logo.ico"
!define MUI_FINISHPAGE_RUN "$INSTDIR\amulet.exe"

!include FileFunc.nsh

Name "Amulet"
OutFile "dist\Amulet-${VERSION}-Windows-x64-installer.exe"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MULTIUSER_PAGE_INSTALLMODE
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

Function .onInit
  !insertmacro MULTIUSER_INIT
FunctionEnd

Function un.onInit
  !insertmacro MULTIUSER_UNINIT
FunctionEnd

Section "install"
    SetOutPath $INSTDIR\lib
    File /r "dist\Amulet\lib\*"
    SetOutPath $INSTDIR
    File "dist\Amulet\amulet.exe"
    File "dist\Amulet\amulet_debug.exe"
    File "logo.ico"
    WriteUninstaller "$INSTDIR\uninstall.exe"
    CreateDirectory "$SMPROGRAMS\Amulet Team"
    CreateShortCut "$SMPROGRAMS\Amulet Team\Amulet ${VERSION}.lnk" "$INSTDIR\amulet.exe" "" "$INSTDIR\logo.ico"

    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "DisplayName" "Amulet ${VERSION}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "InstallLocation" "$\"$INSTDIR$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "DisplayIcon" "$\"$INSTDIR\logo.ico$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "Publisher" "Amulet Team"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "DisplayVersion" "${VERSION}"
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "VersionMajor" 0
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "VersionMinor" 10
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "NoRepair" 1
    ${GetSize} "$INSTDIR" "/S=0K /G=1" $0 $1 $2
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "EstimatedSize" $0
SectionEnd

Section "uninstall"
    Delete "$SMPROGRAMS\Amulet Team\Amulet ${VERSION}.lnk"
    RMDir "$SMPROGRAMS\Amulet Team"
    Delete $INSTDIR\amulet.exe
    Delete $INSTDIR\amulet_debug.exe
    Delete $INSTDIR\logo.ico
    RMDir /r $INSTDIR\lib
    Delete $INSTDIR\uninstall.exe
    RMDir $INSTDIR
    RMDir $INSTDIR\..

    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}"
SectionEnd
