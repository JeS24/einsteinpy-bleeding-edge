!************************************************************
module constants
!********************************************************************
!*    This module defines many constants often uesd in our code.
!*    One can use these constants through a command "use constants" in their
!*    own subroutines or functions. 
!********************************************************************
implicit none
Double precision  infinity,pi,dtors,sixteen,twopi,zero,one,two,three,four,six,half,&
    half2,mh,hbar,pho_v,plankc,five,dtor,eight        
parameter(infinity=1.D40,dtors=asin(1.D0)*2.D0/180.D0, &
    sixteen=16.D0, twopi=4.D0*dasin(1.D0), pi = dasin(1.D0)*2.D0)!3.141592653589793D0
PARAMETER(zero=0.D0, one=1.D0, two=2.D0, three=3.D0, four=4.D0, six=6.D0, half=0.5D0, half2=0.25D0, &
    mh=1.6726231D-24, hbar = 1.0545887D-27, plankc=6.626178D-27, pho_v=2.99792458D10, five=5.D0,&
        dtor=asin(1.D0)*2.D0/180.D0, eight=8.D0)    
!********************************************************************************************
end module constants 
!********************************************************************************************

!********************************************************************************************
module rootsfinding
!********************************************************************
!* This module aim on solve cubic and quartic polynomial equations.
!* One can use these subroutine root3 and root4 to find roots of cubic and 
!* quartic equations respectively. 
!********************************************************************
use constants
implicit none

contains
!*********************************************************************************************
subroutine root3(b,c,d,r1,r2,r3,del)
!********************************************************************
!* PURPOSE:  This subroutine aim on solving cubic equations: x^3+b*x^2+c*x+d=0.
!* INPUTS:    b, c, d-----they are the coefficients of equation. 
!* OUTPUTS:   r1,r2,r3----roots of the equation, with complex number form.
!*            del---------the number of real roots among r1,r2,r3. 
!* ROUTINES CALLED:  sort    
!* This code comes from internet.
!********************************************************************
implicit none
Double precision a,b,c,d,p,q,delta,DD,e1,e2,e3,realp,imagep,temp1,temp2,phi,y1,y2,&
        y3,y2r,y2i,u,v
complex*16 r1,r2,r3
integer del
!f2py intent(in) b,c,d
!f2py intent(out) r1,r2,r3,del

a=1.D0        
! Step 1: Calculate p and q --------------------------------------------
p  = c/a - b*b/a/a/3.D0
q  = (two*b*b*b/a/a/a - 9.D0*b*c/a/a + 27.D0*d/a) / 27.D0

! Step 2: Calculate DD (discriminant) ----------------------------------
DD = p*p*p/27.D0 + q*q/4.D0

! Step 3: Branch to different algorithms based on DD -------------------
if(DD .lt. 0.D0)then
!         Step 3b:
!         3 real unequal roots -- use the trigonometric formulation
    phi = acos(-q/two/sqrt(abs(p*p*p)/27.D0))
    temp1=two*sqrt(abs(p)/3.D0)
    y1 =  temp1*cos(phi/3.D0)
    y2 = -temp1*cos((phi+pi)/3.D0)
    y3 = -temp1*cos((phi-pi)/3.D0)
else
!         Step 3a:
!         1 real root & 2 conjugate complex roots OR 3 real roots (some are equal)
    temp1 = -q/two + sqrt(DD)
    temp2 = -q/two - sqrt(DD)
    u = abs(temp1)**(1.D0/3.D0)
    v = abs(temp2)**(1.D0/3.D0)
    if(temp1 .lt. 0.D0) u=-u
    if(temp2 .lt. 0.D0) v=-v
    y1  = u + v
    y2r = -(u+v)/two
    y2i =  (u-v)*sqrt(3.D0)/two
endif
! Step 4: Final transformation -----------------------------------------
temp1 = b/a/3.D0
y1 = y1-temp1
y2 = y2-temp1
y3 = y3-temp1
y2r=y2r-temp1
! Assign answers -------------------------------------------------------
if(DD .lt. 0.D0)then
    call sort(y1,y2,y3,y1,y2,y3)
    r1 = dcmplx( y1,  0.D0)
    r2 = dcmplx( y2,  0.D0)
    r3 = dcmplx( y3,  0.D0)
    del=3
elseif(DD .eq. 0.D0)then
    call sort(y1,y2r,y2r,y1,y2r,y2r)
    r1 = dcmplx( y1,  0.D0)
    r2 = dcmplx(y2r,  0.D0)
    r3 = dcmplx(y2r,  0.D0)
    del=3
else
    r1 = dcmplx( y1,  0.D0)
    r2 = dcmplx(y2r, y2i)
    r3 = dcmplx(y2r,-y2i)
    del=1
endif
return
end subroutine root3       
!*********************************************************************************************
subroutine root4(b,c,d,e,r1,r2,r3,r4,reals)
!********************************************************************************************* 
!* PURPOSE:  This subroutine aim on solving quartic equations: x^4+b*x^3+c*x^2+d*x+e=0.
!* INPUTS:    b, c, d, e-----they are the coefficients of equation. 
!* OUTPUTS:   r1,r2,r3,r4----roots of the equation, with complex number form.
!*           reals------------the number of real roots among r1,r2,r3,r4.  
!* ROUTINES CALLED:  root3   
!* AUTHOR:     Yang, Xiao-lin & Wang, Jian-cheng (2012)
!* DATE WRITTEN:  1 Jan 2012 
!********************************************************************
implicit none
Double precision b,c,d,e,q,r,s,realp,imagep,two
parameter(two=2.D0)
complex*16 r1,r2,r3,r4,s1,s2,s3,temp(1:4),temp1
integer i,j,del,reals
                    
reals=0
q=c-3.D0*b**2/8.D0
r=d-b*c/two+b**3/8.D0
s=e-b*d/4.D0+b**2*c/16.D0-3.D0*b**4/256.D0
call root3(two*q,q**2-4.D0*s,-r**2,s1,s2,s3,del)

If(del.eq.3)then
    If(real(s3).ge.0.D0)then
        reals=4
        s1=dcmplx(real(sqrt(s1)),0.D0)                
        s2=dcmplx(real(sqrt(s2)),0.D0)                
        s3=dcmplx(real(sqrt(s3)),0.D0)
    else
        reals=0
        s1=sqrt(s1)                
        s2=sqrt(s2)        
        s3=sqrt(s3)
    endif
else
    If(real(s1).ge.0.D0)then
        reals=2
        s1=dcmplx(real(sqrt(s1)),0.D0)
        s2=sqrt(s2)
        s3=dcmplx(real(s2),-aimag(s2))                 
    else
        reals=0
        s1=sqrt(s1)                
        s2=sqrt(s2)        
        s3=sqrt(s3)
    endif 
endif 

if(real(s1*s2*s3)*(-r) .lt. 0.D0)then
    s1=-s1
end if
temp(1)=(s1+s2+s3)/two-b/4.D0
temp(2)=(s1-s2-s3)/two-b/4.D0
temp(3)=(s2-s1-s3)/two-b/4.D0
temp(4)=(s3-s2-s1)/two-b/4.D0

Do i=1,4
    Do j=1+i,4
        If(real(temp(i)).gt.real(temp(j)))then
            temp1=temp(i)
            temp(i)=temp(j)
            temp(j)=temp1
        endif                
    enddo                
enddo
r1=temp(1)
r2=temp(2)
r3=temp(3)
r4=temp(4)
return
end subroutine root4
!*********************************************************************************************
subroutine sort(a1,a2,a3,s1,s2,s3)
!********************************************************************
!* PURPOSE:  This subroutine aim on sorting a1, a2, a3 by decreasing way.
!* INPUTS:    a1,a2,a3----they are the number list required to bo sorted. 
!* OUTPUTS:   s1,s2,s3----sorted number list with decreasing way. 
!*      
!* AUTHOR:     Yang, Xiao-lin & Wang, Jian-cheng (2012)
!* DATE WRITTEN:  1 Jan 2012 
!********************************************************************
implicit none

Double precision s1,s2,s3,s4,temp,arr(1:3),a1,a2,a3
integer i,j

arr(1)=a1
arr(2)=a2
arr(3)=a3

Do i=1,3
    Do j=i+1,3
        If(arr(i)<arr(j))then
            temp=arr(i)
            arr(i)=arr(j)
            arr(j)=temp
        end if     
    end do 
end do
s1=arr(1)
s2=arr(2)
s3=arr(3)
end subroutine sort
end module rootsfinding
!*******************************************************************************