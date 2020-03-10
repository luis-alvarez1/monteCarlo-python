c !  subroutine to save a 1-d array as a 2-d grid, including nodata values
c !  By Rex L. Baum USGS, December 2000, latest revision 27 May 2008
c !  
	subroutine ssvgrd(z3,grd,z2,nrow,ncol,u,nodata,param,u1,
     +	outfil,ti,header)
	implicit none
	integer i,j,nrow,ncol,u,grd,ctr,u1,ia,m
c !  Map 2-d array, z2, onto 1-d array, z3.
c !  Reverse rows and columns, because Fortran stores arrays
c !  by column.  z2 includes nodata values and is used to map
c !  z3 to the grid format
	real z2(ncol,nrow),z3(grd),nodata
	double precision test, param(6),ti,a
	character*14 header(6)
	character*1 sp
	character*255 outfil
 	character*31 scratch
	sp=char(32)
	ctr=0
c !  open and initialize output grid files 
	open (u,file=outfil, status='unknown',err=20)
	do 100, m=1,6
	     a=param(m)
	     ia=int(param(m))
	     if(abs(a-ia).le.ti) then
 	      write(scratch,'(i16)') ia
	     else
 	      write(scratch,*) a
	     end if
	  scratch=adjustl(scratch)
	  write(u,1012) trim(header(m)),trim(scratch)
  100	continue
c !  write grid 
  	do 120, i=1,nrow
	do 110, j=1,ncol
	test=abs(z2(j,i)-nodata)
  	if (test.le.0.1)then
  	  write(scratch,1004) z2(j,i)
	  scratch=adjustl(scratch)
  	  if(j.ne.ncol) then
  	  write(u,1010) trim(scratch),sp 
 	  else
 	  write(u,1011) trim(scratch) 
 	  end if
  	else
  	  ctr=ctr+1
   	  if (z3(ctr).eq.0)  then
  	   write(scratch,1003) z3(ctr)
  	  else
   	   write(scratch,1004) z3(ctr)
 	  end if
	  scratch=adjustl(scratch)
 	  if(j.ne.ncol) then
  	    write(u,1010) trim(scratch),sp 
 	  else
 	    write(u,1011) trim(scratch) 
 	  end if
  	end if
  110	continue
  120	continue
     	close (u)
 	return
   20	continue
  	write (*,*) 'Error opening output file'
	write (*,*) '--> ',outfil
	write (*,*) 'Check file name and status'
  	write (u1,*) 'Error opening output file'
	write (u1,*) '--> ',outfil
	write (u1,*) 'Check file name and status'
	pause 'Press RETURN to exit'
	stop
 1003	format(f2.0)
 1004	format(g12.4)
 1005	format(i)
 1010	format(a,a,$)
 1011	format(a)
 1012	format(t1,a,t15,a)
	end
