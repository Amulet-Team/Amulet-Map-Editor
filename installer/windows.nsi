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
!include LogicLib.nsh

Name "Amulet"
OutFile "dist\Amulet-${VERSION}-Windows-x64.exe"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MULTIUSER_PAGE_INSTALLMODE

Function DisableDirIfAllUsers
    ${If} $MultiUser.InstallMode == "AllUsers"
        FindWindow $1 "#32770" "" $HWNDPARENT
        GetDlgItem $0 $1 1001
        EnableWindow $0 0
        GetDlgItem $0 $1 1019
        EnableWindow $0 0
    ${EndIf}
FunctionEnd

Function CheckInstallDir
    IfFileExists "$INSTDIR\*.*" 0 ok
        ${If} $MultiUser.InstallMode == "AllUsers"
            MessageBox MB_ICONSTOP "This version of Amulet is already installed.$\nPlease uninstall it before installing it again."
        ${Else}
            MessageBox MB_ICONSTOP "Amulet must be installed to an empty directory.$\nPlease select an empty directory or uninstall Amulet from this directory first."
        ${EndIf}
        Abort
ok:
FunctionEnd

!define MUI_PAGE_CUSTOMFUNCTION_SHOW DisableDirIfAllUsers
!define MUI_PAGE_CUSTOMFUNCTION_LEAVE CheckInstallDir
!insertmacro MUI_PAGE_DIRECTORY

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
    File /r "dist\amulet\lib\*"
    SetOutPath $INSTDIR
    File "dist\amulet\amulet.exe"
    File "dist\amulet\amulet_debug.exe"
    File "logo.ico"
    WriteUninstaller "$INSTDIR\uninstall.exe"
    CreateDirectory "$SMPROGRAMS\Amulet Team"
    CreateShortCut "$SMPROGRAMS\Amulet Team\Amulet ${VERSION}.lnk" "$INSTDIR\amulet.exe" "" "$INSTDIR\logo.ico"

    WriteRegStr SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "DisplayName" "Amulet ${VERSION}"
    WriteRegStr SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
    WriteRegStr SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
    WriteRegStr SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "InstallLocation" "$\"$INSTDIR$\""
    WriteRegStr SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "DisplayIcon" "$\"$INSTDIR\logo.ico$\""
    WriteRegStr SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "Publisher" "Amulet Team"
    WriteRegStr SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "DisplayVersion" "${VERSION}"
    WriteRegDWORD SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "VersionMajor" 0
    WriteRegDWORD SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "VersionMinor" 10
    WriteRegDWORD SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "NoModify" 1
    WriteRegDWORD SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "NoRepair" 1
    ${GetSize} "$INSTDIR" "/S=0K /G=1" $0 $1 $2
    WriteRegDWORD SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}" "EstimatedSize" $0
SectionEnd

Section "uninstall"
    ;Detect if we are installed for all users
    StrCpy $0 "$PROGRAMFILES64\"
    StrLen $1 $0
    StrCpy $2 $INSTDIR $1
    ${IF} $0 == $2
        SetShellVarContext all
    ${Else}
        SetShellVarContext current
    ${EndIf}

    Delete "$SMPROGRAMS\Amulet Team\Amulet ${VERSION}.lnk"
    RMDir "$SMPROGRAMS\Amulet Team"
    Delete "$INSTDIR\amulet.exe"
    Delete "$INSTDIR\amulet_debug.exe"
    Delete "$INSTDIR\logo.ico"
    RMDir /r "$INSTDIR\lib"
    Delete "$INSTDIR\uninstall.exe"
    RMDir "$INSTDIR"
    RMDir "$INSTDIR\.."

    DeleteRegKey SHCTX "Software\Microsoft\Windows\CurrentVersion\Uninstall\Amulet ${VERSION}"
SectionEnd
