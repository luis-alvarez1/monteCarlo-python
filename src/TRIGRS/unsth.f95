! compute K, Pressure head and volumetric water content in the unsaturated zone
! uses analytic solution for normalized transmissivity
! By Rex L. Baum and W.Z. Savage, USGS
	subroutine unsth(i,j1,ncc,iper,t1,nmx1,lcv,ulog,vqt,delh,nmn1,sqin,vqtn)
	use model_vars; use input_vars 
	use grids
	implicit none
	integer::i,j,j1,k,k1,m,ncc,nmx1,nmn1,iper,ulog 
	logical lcv,lnu
	real (double):: t1,d,sqin
	real (double):: al,cks,cths,cthr,tf,zns,qa,rslo,b1 
	real (double):: z,zinc,tstar,tdif1,tdif2,kas,kbs,ka,kb 
	real (double):: k2a,k2b,k2old,bot,top,delk,tol 
	real (double):: derfc,ck0,f0,ft,f1,f1a,f1b,f1c 
	real (double):: f2,f2a,f2b,f2c,arg1,arg2,cn,psi0,th0,tstar1
	real (double):: vfil,trvty,vqt,vqtn,vdif1 
	real (double):: vdif,vhi,zhi,vlo,zlo,vf(nzs+1),dusznew,delh
	real (double):: vfa(nzs+1),trsa,trsb,trva,trvb
	real (double):: trold,trbot,tra,trb,tr1,tr2,deltr,qlb
	real (double):: trtop,trtop1,trtop2,trtop3,ck1  
	tol=1.0e-06
	rslo=slo(i)
	b1=cos(rslo)
 	al=alp(zo(i))
 	al=al*b1*b1 ! for coordinate transformation
 	cks=ks(zo(i))
 	qlb=cks
 	qa=cks*rikzero(i)
 	cths=ths(zo(i))
 	cthr=thr(zo(i))
	tf=al*cks/(cths-cthr)
	zns=float(nzs)
	zinc=(zmax(i)-zmin)/zns
	z=zmin
	pzero=0.
	d=dusz
	kz=0.;trz=0.
	Z_loop: do j=1,nzs+1
	  kas=0.;kbs=0.
	  trsa=0.;trsb=0.
	  if(z >= d) then 
	    kz(j)=cks
	    thz(j)=cths
	    trz(j)=(zmax(i)-z)*cks
	    z=z+zinc
	    cycle
	  end if
	  ck0=qa-(qa-cks)*exp(-al*(d-z))
	  psi0=log(ck0/cks)/al
          th0=cthr+(cths-cthr)*exp(al*psi0)
   	  f0=-(q(j1)-qa)*exp(al*(d-z)/2.)
	  ft=0.0
	  t_loop: do m=1,iper
	    delk=0.;deltr=0.
      	    tdif1=t1-capt(m)
	    if(tdif1 > 1.0e-10) then ! effectively zero
	      tstar=tf*tdif1
	      tstar1=tstar
	      if(tstar < smt) then ! early-time solution
		cn=float(2*m-1)	
	        arg1=al*(cn*d-z)/(2.*sqrt(tstar))
	        f1a=exp(-tstar/4.)*derfc(arg1)
	        f1b=exp(arg1*sqrt(tstar))
	        f1c=derfc(arg1+sqrt(tstar/4.))
	        f1=f1a-f1b*f1c
        	ka=ck0+2.*f1*f0 
        	trva=ka*zinc ! approximate formula for  normalized transmissivity
	      else ! later-time series solution
	        k2a=0.d0; tra=0.d0
	        k_series_a: do k=1,nmax
   		  top=sin(r(k)*al*(d-z))*sin(r(k)*al*d)*&
		   &exp(-(r(k)**2)*tstar)
		  bot=1.+al*d/2.+2.*al*d*r(k)**2
	          k2old=k2a
	          k2a=k2a+top/bot
	          delk=abs((k2a-k2old)/k2a)
	          trtop1=sin(al*r(k)*(d-z))+2.*r(k)*&
		  &cos(r(k)*al*(d-z))
	          trtop2=2.*r(k)*exp(al*d/2.)-exp(al*z/2.)*trtop1
                  trtop3=sin(r(k)*al*d)*exp(-(r(k)**2)*tstar)
	          trtop=trtop2*trtop3
	          trbot=(r(k)**2+1./4.)*bot
	          trold=tra
	          tra=tra+trtop/trbot 
	          deltr=abs((tra-trold)/tra)
	          k1=k
	          if(delk<=tol .and. deltr<=tol) exit k_series_a
	        end do k_series_a
	        if(lcv .and. delk>tol) then
	          ncc=ncc+1
	          nvu(i)=1
	          lcv=.false.
                  write(*,*) 'noncv_th1!', k1,t1,tdif1,delk,k2a
	        end if
 		f1=2.*(q(m)-qa)*exp(al*z/2.)*exp(-tstar/4.)
		ck1=q(m)-(q(m)-qlb)*exp(-al*(d-z))
        	ka=ck1-2.*f1*k2a
	        tr1=q(m)*(d-z)-(q(m)-qlb)*(1.0-exp(-al*(d-z)))/al
  	        tr2=2.*(q(m)-qa)*exp(-tstar/4.)/al
	        trva=tr1-tr2*tra
	      end if
	      if(k1>nmx1) nmx1=k1
	      if(k1<nmn1) nmn1=k1
	    else
	      ka=0.0
	      f1=0.0
	      trva=0.0
	    end if
	    kas=kas+ka
	    trsa=trsa+trva
	    tdif2=t1-capt(m+1)
	    if(tdif2 > 1.0e-10) then ! effectively zero
	      tstar=tf*tdif2
	      if(tstar < smt) then ! early-time solution
		arg2=al*(cn*d+z)/(2.*sqrt(tstar))
		f2a=exp(-tstar/4.)*derfc(arg2)
		f2b=exp(arg2*sqrt(tstar))
		f2c=derfc(arg2+sqrt(tstar/4.))
		f2=f2a-f2b*f2c
        	kb=ck0+2.*f2*f0 
        	trvb=ka*zinc ! approximate formula for normalized transmissivity
	      else ! later-time series solution
	        k2b=0.d0; trb=0.d0
	        k_series_b: do k=1,nmax
   		  top=sin(r(k)*al*(d-z))*sin(r(k)*al*d)*&
		    &exp(-(r(k)**2)*tstar)
		  bot=1.+al*d/2.+2.*al*d*r(k)**2
	          k2old=k2b
	          k2b=k2b+top/bot
	          delk=abs((k2b-k2old)/k2b)
	          trtop1=sin(al*r(k)*(d-z))+2.*r(k)*&
		  &cos(r(k)*al*(d-z))
	          trtop2=2.*r(k)*exp(al*d/2.)-exp(al*z/2.)*trtop1
                  trtop3=sin(r(k)*al*d)*exp(-(r(k)**2)*tstar)
	          trtop=trtop2*trtop3
	          trbot=(r(k)**2+1./4.)*bot
	          trold=trb
	          trb=trb+trtop/trbot 
	          deltr=abs((trb-trold)/trb)
	          k1=k
	          if(delk<=tol .and. deltr<=tol) exit k_series_b
	        end do k_series_b
	        if(lcv .and. delk>tol) then
	          ncc=ncc+1
	          nvu(i)=1
	          lcv=.false.
                  write(*,*) 'noncv_th2!', k1,t1,tdif2,delk,k2b
	        end if
 		f1=2.*(q(m)-qa)*exp(al*z/2.)*exp(-tstar/4.)
		ck1=q(m)-(q(m)-qlb)*exp(-al*(d-z))
        	kb=ck1-2.*f1*k2b
	        tr1=q(m)*(d-z)-(q(m)-qlb)*(1.0-exp(-al*(d-z)))/al
  	        tr2=2.*(q(m)-qa)*exp(-tstar/4.)/al
	        trvb=tr1-tr2*trb
	      end if
	      if(k1>nmx1) nmx1=k1
	      if(k1<nmn1) nmn1=k1
	    else
	      kb=0.0
	      f2=0.0
	      trvb=0.0
	    end if
	    kbs=kbs+kb
	    trsb=trsb+trvb
	  end do t_loop  
	  if(t1==0.) then
	    kz(j)=ck0
      	    ptran(j)=psi0*b1
! Analytic formulas for normalized transmissivity, trz()      	    
      	    if(lps0) then 
	      trz(j)=qa*(d-z)+(qa-cks)*(exp(-al*(d-z))-1)/al ! use if psi0=-1/al
	    else
	      trz(j)=qa*(d-z)+(qa-cks)*(exp(-al*(d-z))-1)/al ! use if psi0=0
	    end if
	  else
	    kz(j)=kz(j)+kas-kbs
	    trz(j)=trz(j)+trsa-trsb
	  end if
! confirm that ptran(j)<0
	  if(kz(j)>0.) then
	    if(lps0) then ! multipliying by b1* corrects for slope
	      ptran(j)=b1*(log(kz(j)/cks)-1.)/al ! use if psi0=-1/al
	    else
	      ptran(j)=b1*(log(kz(j)/cks))/al ! use if psi0=0
	    end if
	  else
	    ptran(j)=-b1/al 
	  end if	  
	  thz(j)=cthr+(cths-cthr)*exp(al*ptran(j)) 
	  if (thz(j)>cths) thz(j)=cths
	  z=z+zinc
	end do Z_loop
	z=zmax(i)-zinc
	vfil=0.;vf(nzs+1)=0.;vfa(nzs+1)=0.
! Numerical integration of normalized transmissivity (trvty)
	trvty=-(zmax(i)-d)*cks 
	do j=nzs,1,-1
	  trvty=trvty+zinc*(kz(j)+kz(j+1))/2. 
	  if(tstar1 < smt) then
	    trz(j)=trvty
	  end if
	  if(z>=d) then
	    vf(j)=0.
	  else
	    vf(j)=(cths-cthr)*((d-z)-trvty/cks) 
	    if(vf(j)<0.) vf(j)=-vf(j)
	  end if
	  if(z>d) then
	    vfa(j)=0.
	  else
	    vfa(j)=(cths-cthr)*((d-z)-trz(j)/cks) 
	    if(vfa(j)<0.) vfa(j)=-vfa(j)
	  end if
	  z=z-zinc
	end do
	lnu=.true.
	if(lany) vf=vfa
	if(t1==0.) vf0=vf(1)
	if(vqt>0.) then
	  z=zmin; vlo=0.; vhi=cths*zmax(i)
	  do j=1,nzs 
	    if(vf(j)>0.) then
	      vdif=vf(j)-vqt
	      if(vdif==0.) then
	        dusznew=z
	        exit
	      else if(vdif>0.) then
	        vdif1=vf(j+1)-vqt
	        if(vdif1<0) then
	          vhi=vf(j)
	          zhi=z
	          vlo=vf(j+1)
	          zlo=z+zinc
	        end if
	      end if  
	    end if
	    z=z+zinc
	  end do
	  if(vqt>vf(1)) then
	    zlo=zmax(i)
	    zhi=0.
	    vhi=vqt
	    vlo=0.
	  end if
	else
	  lnu=.false.
	end if
	delh=0.
	if(llus) then ! estimate water-table rise
	  if(lnu) then
	    if(zlo<d) then
	      dusznew=zhi+zinc*(vhi-vqt)/(vhi-vlo)
	    else
	      dusznew=d-zinc*(vqt)/(vhi-vlo)
	    end if
	    delh=d-dusznew
	    if(depth(i)>zmax(i)) delh=delh-(depth(i)-zmax(i)) ! accounts for initial wt below zmax(i)
	    if(vqt>vf(1)) then
	      dusznew=0.
	      delh=depth(i)-dusznew
	    end if
	  else 
	    delh=0.
	    dusznew=d-delh
	  end if
	end if
	if(outp(8)) write (ulog,*) t1,sqin,t1*rizero(i),vqtn,vf0-vf(1),sqin-vqtn-t1*rizero(i),vqt,delh
	return
	end subroutine unsth
