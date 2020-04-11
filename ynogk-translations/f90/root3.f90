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