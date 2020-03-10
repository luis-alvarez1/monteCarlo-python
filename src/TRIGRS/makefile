
#
# Absoft Developer Tools Interface requires use of this makefile.
#
MKDIR=if not exist "$(OBJDIR)\nul" mkdir 
RMDIR=rmdir /S /Q

#
# Variables for the compiler(s) and linker
#
ABSOFT_F95=f95
ABSOFT_F77=f95
VAST_PREPROCESSOR=vastfp.exe 
RC=rc.exe
CL=cl.exe
ABSOFT_F95_LINKER=f95
DUMMY=

#
# Flags
#
ABSOFT_F95_FLAGS=-m32 -s -YVAR_NAMES=LCS -O2
ABSOFT_F77_FLAGS=-O2 -YVAR_NAMES=LCS -s -m32 -f77_compat
RC_FLAGS=
CL_FLAGS=-O2
ABSOFT_F95_LINKER_FLAGS=-m32 -O2

#
# Name of the executable
#
TARGET=trigrs.exe
OUTDIR=.
OBJDIR=.\Release

#
# Files for this executable
#
VAST_PREPROCESSOR_FILES=
ABSOFT_F95_FILES="dsimps.f95" "flux.f90" "grids.f95" "input_file_defs.f95" "input_vars.f95" "iverson.f95" "ivestp.f95" "model_vars.f95" "pstpf.f95" "pstpi.f95" "rnoff.f95" "satfin.f95" "satinf.f95" "savage.f95" "smallt.f95" "steady.f95" "svgstp.f95" "trigrs.f90" "trini.f95" "unsfin.f95" "unsinf.f95" "unsth.f95"
ABSOFT_F77_FILES="dbsct.f" "derfc.f" "irdgrd.f" "irdswm.f" "isvgrd.f" "calerf.f" "roots.f" "srdgrd.f" "srdswm.f" "ssvgrd.f"
CL_FILES=
ABSOFT_F95_LINKER_FILES=
RC_FILES=

#
# Rules and dependencies for the executable
#
SRCFILES=$(ABSOFT_F95_FILES) $(ABSOFT_F77_FILES)
OBJFILES="$(OBJDIR)\dsimps.obj" "$(OBJDIR)\flux.obj" "$(OBJDIR)\grids.obj" "$(OBJDIR)\input_file_defs.obj" "$(OBJDIR)\input_vars.obj" "$(OBJDIR)\iverson.obj" "$(OBJDIR)\ivestp.obj" "$(OBJDIR)\model_vars.obj" "$(OBJDIR)\pstpf.obj" "$(OBJDIR)\pstpi.obj" "$(OBJDIR)\rnoff.obj" "$(OBJDIR)\satfin.obj" "$(OBJDIR)\satinf.obj" "$(OBJDIR)\savage.obj" "$(OBJDIR)\smallt.obj" "$(OBJDIR)\steady.obj" "$(OBJDIR)\svgstp.obj" "$(OBJDIR)\trigrs.obj" "$(OBJDIR)\trini.obj" "$(OBJDIR)\unsfin.obj" "$(OBJDIR)\unsinf.obj" "$(OBJDIR)\unsth.obj" "$(OBJDIR)\dbsct.obj" "$(OBJDIR)\derfc.obj" "$(OBJDIR)\irdgrd.obj" "$(OBJDIR)\irdswm.obj" "$(OBJDIR)\isvgrd.obj" "$(OBJDIR)\calerf.obj" "$(OBJDIR)\roots.obj" "$(OBJDIR)\srdgrd.obj" "$(OBJDIR)\srdswm.obj" "$(OBJDIR)\ssvgrd.obj"
all: "$(OUTDIR)\$(TARGET)"
	

"$(OUTDIR)\$(TARGET)": "$(OBJDIR)" $(OBJFILES) $(USER_LIBS) $(MODFILES) $(RC_FILES)
	$(ABSOFT_F95_LINKER) $(ABSOFT_F95_LINKER_FLAGS) $(LPATHS) $(OBJFILES) $(ABSOFT_F95_LINKER_FILES) $(LIBS) -o "$(OUTDIR)\$(TARGET)"



"$(OBJDIR)\dsimps.obj": "dsimps.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\dsimps.obj" "dsimps.f95"

"$(OBJDIR)\flux.obj": "flux.f90"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\flux.obj" "flux.f90"

"$(OBJDIR)\grids.obj": "grids.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\grids.obj" "grids.f95"

"$(OBJDIR)\input_file_defs.obj": "input_file_defs.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\input_file_defs.obj" "input_file_defs.f95"

"$(OBJDIR)\input_vars.obj": "input_vars.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\input_vars.obj" "input_vars.f95"

"$(OBJDIR)\iverson.obj": "iverson.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\iverson.obj" "iverson.f95"

"$(OBJDIR)\ivestp.obj": "ivestp.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\ivestp.obj" "ivestp.f95"

"$(OBJDIR)\model_vars.obj": "model_vars.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\model_vars.obj" "model_vars.f95"

"$(OBJDIR)\pstpf.obj": "pstpf.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\pstpf.obj" "pstpf.f95"

"$(OBJDIR)\pstpi.obj": "pstpi.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\pstpi.obj" "pstpi.f95"

"$(OBJDIR)\rnoff.obj": "rnoff.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\rnoff.obj" "rnoff.f95"

"$(OBJDIR)\satfin.obj": "satfin.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\satfin.obj" "satfin.f95"

"$(OBJDIR)\satinf.obj": "satinf.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\satinf.obj" "satinf.f95"

"$(OBJDIR)\savage.obj": "savage.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\savage.obj" "savage.f95"

"$(OBJDIR)\smallt.obj": "smallt.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\smallt.obj" "smallt.f95"

"$(OBJDIR)\steady.obj": "steady.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\steady.obj" "steady.f95"

"$(OBJDIR)\svgstp.obj": "svgstp.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\svgstp.obj" "svgstp.f95"

"$(OBJDIR)\trigrs.obj": "trigrs.f90"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\trigrs.obj" "trigrs.f90"

"$(OBJDIR)\trini.obj": "trini.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\trini.obj" "trini.f95"

"$(OBJDIR)\unsfin.obj": "unsfin.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\unsfin.obj" "unsfin.f95"

"$(OBJDIR)\unsinf.obj": "unsinf.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\unsinf.obj" "unsinf.f95"

"$(OBJDIR)\unsth.obj": "unsth.f95"
	$(ABSOFT_F95) -c -nowdir $(ABSOFT_F95_FLAGS) -o "$(OBJDIR)\unsth.obj" "unsth.f95"

"$(OBJDIR)\dbsct.obj": "dbsct.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\dbsct.obj" "dbsct.f"

"$(OBJDIR)\derfc.obj": "derfc.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\derfc.obj" "derfc.f"

"$(OBJDIR)\irdgrd.obj": "irdgrd.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\irdgrd.obj" "irdgrd.f"

"$(OBJDIR)\irdswm.obj": "irdswm.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\irdswm.obj" "irdswm.f"

"$(OBJDIR)\isvgrd.obj": "isvgrd.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\isvgrd.obj" "isvgrd.f"

"$(OBJDIR)\calerf.obj": "calerf.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\calerf.obj" "calerf.f"

"$(OBJDIR)\roots.obj": "roots.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\roots.obj" "roots.f"

"$(OBJDIR)\srdgrd.obj": "srdgrd.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\srdgrd.obj" "srdgrd.f"

"$(OBJDIR)\srdswm.obj": "srdswm.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\srdswm.obj" "srdswm.f"

"$(OBJDIR)\ssvgrd.obj": "ssvgrd.f"
	$(ABSOFT_F77) -c -nowdir $(ABSOFT_F77_FLAGS) -o "$(OBJDIR)\ssvgrd.obj" "ssvgrd.f"

"$(OBJDIR)":
	$(MKDIR) "$(OBJDIR)"
#
# Clean Rules
#
clean:
	 if exist "$(OBJDIR)" $(RMDIR) "$(OBJDIR)" 
	 if exist "$(TARGET)" erase "$(TARGET)"

#
# Define necessary macros for dependency scanning.
#
MKDEP=amakedepend
MKDEP_FLAGS= -quiet "-pre$(OBJDIR)\"\" -Y -modInfo -errdel -f90 -f makefile 
#
# Generate dependencies for the project
#
ScanAll: "$(OUTDIR)" "$(OBJDIR)" MakeDepsAll

#
# Scan for all F77, F95, and c/c++ dependencies
#
MakeDepsAll:
	$(MKDEP) "@C:\Documents and Settings\baum\My Documents\Fortran code\TRIGRS_suite_v2\TRIGRS_v2\Release\mkdep_F95"
	$(MKDEP) "@C:\Documents and Settings\baum\My Documents\Fortran code\TRIGRS_suite_v2\TRIGRS_v2\Release\mkdep_F77"
# DO NOT DELETE THIS LINE - makedepend depends upon it.



".\Release\grids.obj"&: ".\Release\grids.mod"

".\Release\input_file_defs.obj"&: ".\Release\input_file_defs.mod"

".\Release\input_vars.obj"&: ".\Release\input_vars.mod"



".\Release\model_vars.obj"&: ".\Release\model_vars.mod"















# Defined Module: .\Release\grids.mod
# Defined Module: .\Release\input_file_defs.mod
# Defined Module: .\Release\input_vars.mod
# Defined Module: .\Release\model_vars.mod

".\Release\flux.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\flux.obj": ".\Release\model_vars.mod"




".\Release\iverson.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\iverson.obj": ".\Release\model_vars.mod"

".\Release\ivestp.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\ivestp.obj": ".\Release\model_vars.mod"


".\Release\pstpf.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\pstpf.obj": ".\Release\model_vars.mod"

".\Release\pstpi.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\pstpi.obj": ".\Release\model_vars.mod"

".\Release\rnoff.obj": ".\Release\input_file_defs.mod"
".\Release\rnoff.obj": ".\Release\input_vars.mod" ".\Release\grids.mod"

".\Release\satfin.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\satfin.obj": ".\Release\model_vars.mod"
".\Release\satfin.obj": ".\Release\input_file_defs.mod"

".\Release\satinf.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\satinf.obj": ".\Release\model_vars.mod"
".\Release\satinf.obj": ".\Release\input_file_defs.mod"

".\Release\savage.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\savage.obj": ".\Release\model_vars.mod"


".\Release\steady.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"

".\Release\svgstp.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\svgstp.obj": ".\Release\model_vars.mod"

".\Release\trigrs.obj": ".\Release\input_file_defs.mod"
".\Release\trigrs.obj": ".\Release\input_vars.mod" ".\Release\grids.mod"
".\Release\trigrs.obj": ".\Release\model_vars.mod"

".\Release\trini.obj": ".\Release\input_file_defs.mod"
".\Release\trini.obj": ".\Release\input_vars.mod"

".\Release\unsfin.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\unsfin.obj": ".\Release\model_vars.mod"
".\Release\unsfin.obj": ".\Release\input_file_defs.mod"

".\Release\unsinf.obj": ".\Release\grids.mod" ".\Release\input_vars.mod"
".\Release\unsinf.obj": ".\Release\model_vars.mod"
".\Release\unsinf.obj": ".\Release\input_file_defs.mod"

".\Release\unsth.obj": ".\Release\model_vars.mod" ".\Release\input_vars.mod"
".\Release\unsth.obj": ".\Release\grids.mod"




















