import numpy as np

c = 1
a = 0.998
r_s = 2

# // GLOBAL VARIABLES
# ////////////////////
DIM = 4
NDIM = 4
startx = np.zeros(NDIM, dtype=float)
stopx = np.zeros(NDIM, dtype=float)
dx = np.zeros(NDIM, dtype=float)
# real startx[NDIM], stopx[NDIM], dx[NDIM];

#define num_indices 1
num_indices = 1

# // Metric
logscale = False # Standard BL/KS coordinates; no logarithmic radius - ???? FOR NOW
# #define metric   (MKS)
# #if(metric == CAR || metric == BL || metric == KS)
# #define logscale (0)    // Standard BL/KS coordinates; no logarithmic radius
# #elif(metric == MBL || metric == MKS)
# #define logscale (1)    // Modified BL/KS coordinates; logarithmic radius
# #endif

LOG_IMPACT_CAM = False
LINEAR_IMPACT_CAM = True
IMG_WIDTH = 0 ##????
IMG_HEIGHT = 0 ##????
CAM_SIZE_X = 0 ##????
CAM_SIZE_Y = 0 ##????
#define LOG_IMPACT_CAM (0)
#define LINEAR_IMPACT_CAM (1)
# int IMG_WIDTH;
# int IMG_HEIGHT;
# real CAM_SIZE_X;
# real CAM_SIZE_Y;

max_steps = 1e5
# #define max_steps    (1e5)   // Maximum number of integration steps

# //	#define rcam         (15.)//(500.)    // Camera distance from the sing.(units of Rg)
# #define rcam         (1.e4)
rcam = 1e4
#define cutoff_outer (rcam*1.01)    // Outer cutoff, near flat spacetime, in M
cutoff_outer = (rcam * 1.01)
cutoff_inner = 0. ##???? - WHAT VALUE?
# real cutoff_inner; // Inner integration boundary

max_order = 100
#define max_order    (100)       // Maximimum order of lensed image computed (0 = direct only)

# // OBSERVER PARAMETERS
# //////////////////////
INCLINATION = 0. ##???? - WHAT VALUE?
# real INCLINATION;

#define horizon_marg (1e-1)     // Stop tracing at this distance from E.H. [BL]
#define VER       (1)        //
#define RK4       (2)        //
#define RK2      (3)
#define int_method   (RK2)     // method of integration 2=Verlet, 4-RK4

# ******************************************************************************************************


# // Initialize a contravariant photon wave vector based on impact parameters
# // alpha and beta
# // Ref. Cunningham & Bardeen 1973
# // We want to pick E, L, Q based on impact params alpha, beta
# // Then construct k_u using E, L, Q
# // The photons all start at the camera location
def initialize_photon(alpha, beta, photon_u, t_init):
    # (real alpha, real beta, real photon_u[8], real t_init)

        # //    beta *= -1.;
        mu0 = np.cos(INCLINATION / 180. * np.pi)
        Xcam_u = np.array([t_init, np.log(rcam) if logscale else rcam, np.arccos(mu0), 90./180. * np.pi])
        En = 1.
        ll = -alpha * np.sqrt(1. - mu0**2)
        qq = beta**2 + mu0**2 * (alpha**2 - 1.)
        L1 = ll * En
        Q1 = qq * (En**2)
        k_d = np.zeros(4, dtype=float)
        k_u = np.zeros(4, dtype=float)
        sinc2 = np.sin(Xcam_u[2])**2
        cosc2 = np.cos(Xcam_u[2])**2

        # real mu0 = cos(INCLINATION / 180. * M_PI);
        # real Xcam_u[4] = {t_init, logscale ? log(rcam) : rcam, acos(mu0), 90./180. * M_PI};
        # real En = 1.;
        # real E2 = En * En;
        # real ll = -alpha * sqrt(1. - mu0 * mu0);
        # real qq = beta * beta + mu0 * mu0 * (alpha * alpha - 1.);
        # real L1 = ll * En;
        # real Q1 = qq * E2;
        # real k_d[4], k_u[4];
        # real sinc2 = sin(Xcam_u[2]) * sin(Xcam_u[2]);
        # real cosc2 = cos(Xcam_u[2]) * cos(Xcam_u[2]);

        # // Covariant wave vector entries are known:
        k_d[0] = -En
        k_d[3] = L1
        k_d[2] = np.sign(beta) * np.sqrt(np.abs(Q1 - L1 * L1 * (cosc2/sinc2) + (En**2)*cosc2))

        # k_d[0] = -En;
        # k_d[3] = L1;
        # k_d[2] = sign(beta)*sqrt( fabs(Q1 - L1 * L1 * (cosc2/sinc2) + (En**2)*cosc2));

        # // Construct contravariant wave vector k_u using the BL metric
        r       = (rcam) if logscale else rcam
        rfactor = r if logscale else 1.
        # real r       = logscale ? (rcam) : rcam;
        # real rfactor = logscale ? r : 1.;

        theta = np.arccos(mu0)
        sint  = np.sin(theta)
        cost  = np.cos(theta)
        sigma = r**2 + (a * cost)**2
        delta = r**2 + a**2 - 2. * r
        A_    = (r**2 + a**2) * (r**2 + a**2) - delta * a**2 * sint**2
        # real theta = acos(mu0);
        # real sint  = sin(theta);
        # real cost  = cos(theta);
        # real sigma = r * r + a * a * cost * cost;
        # real delta = r * r + a * a - 2. * r;
        # real A_    = (r * r + a * a) * (r * r + a * a) - delta * a * a *
        #              sint * sint;
        

        g_dd_11 = sigma / delta * rfactor**2
        g_uu_00 = -A_ / (sigma * delta)
        g_uu_03 = -2. * a * r / (sigma * delta)
        g_uu_33 = (delta - (a * sint)**2) / (sigma * delta * sint**2)
        g_uu_22 = 1. / sigma
        # real g_dd_11 = sigma / delta * rfactor * rfactor;
        # real g_uu_00 = -A_ / (sigma * delta);
        # real g_uu_03 = -2. * a * r / (sigma * delta);
        # real g_uu_33 = (delta - a * a * sint * sint) /
        #                (sigma * delta * sint * sint);
        # real g_uu_22 = 1. / sigma;

        k_u[0] = g_uu_00 * k_d[0] + g_uu_03 * k_d[3]
        k_u[3] = g_uu_33 * k_d[3] + g_uu_03 * k_d[0]
        k_u[2] = g_uu_22 * k_d[2]
        k_u[1] = np.sqrt((-k_u[0]*k_d[0]-k_u[2]*k_d[2]-k_u[3]*k_d[3]) / g_dd_11)
        # k_u[0] = g_uu_00 * k_d[0] + g_uu_03 * k_d[3];
        # k_u[3] = g_uu_33 * k_d[3] + g_uu_03 * k_d[0];
        # k_u[2] = g_uu_22 * k_d[2];
        # k_u[1] = sqrt((-k_u[0]*k_d[0]-k_u[2]*k_d[2]-k_u[3]*k_d[3]) / g_dd_11);

        # // Normalize the photon wavevector with cam_freq in Hz
        # int i;
        # //    LOOP_i k_u[i] *= PLANCK_CONSTANT * cam_freq /
        # //                   (ELECTRON_MASS * SPEED_OF_LIGHT*SPEED_OF_LIGHT);
        # // Place wave vector into "photon_u"
        photon_u[0] = Xcam_u[0]
        photon_u[1] = Xcam_u[1]
        photon_u[2] = Xcam_u[2]
        photon_u[3] = Xcam_u[3]
        photon_u[4] = k_u[0]
        photon_u[5] = k_u[1]
        photon_u[6] = k_u[2]
        photon_u[7] = k_u[3]
        # photon_u[0] = Xcam_u[0];
        # photon_u[1] = Xcam_u[1];
        # photon_u[2] = Xcam_u[2];
        # photon_u[3] = Xcam_u[3];
        # photon_u[4] = k_u[0];
        # photon_u[5] = k_u[1];
        # photon_u[6] = k_u[2];
        # photon_u[7] = k_u[3];

        # //    printf("\nFirst we build k in BL coords");
        # //    LOOP_i printf("\n%+.15e", photon_u[i]);
        # //    LOOP_i printf("\n%+.15e", photon_u[i+4]);

        # // Convert k_u to the coordinate system that is currently used - ???? NOT NEEDED AS BL/MBL IN USE (AT LEAST FOR NOW)
# #if (metric == KS  || metric == MKS)
#         real KSphoton_u[8];
#         BL_to_KS_u(photon_u, KSphoton_u);
#         LOOP_i {
#                 photon_u[i] = KSphoton_u[i];
#                 photon_u[i+4] = KSphoton_u[i+4];
#         }
# #endif

# #if (metric == MKS )
#         photon_u[2] = Xg2_approx_rand(photon_u[2],photon_u[1],1); // We only transform theta - r is already exponential and R0 = 0
#         photon_u[6] = Ug2_approx_rand(photon_u[6], photon_u[5],photon_u[2],photon_u[1],1); // We only transform theta - r is already exponential and R0 = 0
# #endif


# // Integrate the null geodesic defined by "photon_u"
def integrate_geodesic(icur, x, y, intensityfield2, frequencies, p, t, Xcam, Ucam):
    # (int icur,int x, int y, real intensityfield2[maxsize][num_indices],real *frequencies, real **** p,real t,real Xcam[4],real Ucam[4])
        # // Variables
        f, i, q = 0., 0., 0.
        # int f,i, q;
        t_init = 0.
        # real t_init = 0.;
        dlambda_adaptive = 0.
        # real dlambda_adaptive;
        theta_turns = 0
        # int theta_turns = 0;
        thetadot_prev = 0.
        # real thetadot_prev;
        X_u = np.zeros((4), dtype=float)
        k_u = np.zeros((4), dtype=float)
        # real X_u[4], k_u[4];
        alpha, beta = 0., 0.
        # real alpha,beta;
        tau = np.zeros(num_indices)
        # real tau[num_indices];

        # for( f = 0; f < num_indices; f++) {
        #         tau[f]=0.0;
        #         intensityfield2[icur][f]=0.0; ##????
        # }

        lightpath = np.zeros(15)
        # real lightpath[15];
        # for( i=0; i<15; i++)
        #         lightpath[i]=0;

        steps = 0
        # int steps = 0;

        photon_u = np.zeros(8, dtype=float)
        # real photon_u[8];
        # for( i=0; i<8; i++)
        #         photon_u[i]=0;

        # // "GEOD" means that RAPTOR outputs information about the geodesics it computes.
# #if (GEOD)
#         struct stat st = {0};
#         char geod_folder[256]="";
#         sprintf(geod_folder, "geod");

#         if (stat(geod_folder, &st) == -1) {
#                 mkdir(geod_folder, 0700);
#         }

#         char geod_filename[100];
#         sprintf(geod_filename,"%s/geodesic_%d_%d.dat",geod_folder,x,y);
#         FILE *geod = fopen(geod_filename,"w");
# #endif

        # // Create initial ray conditions
        if LINEAR_IMPACT_CAM:
            stepx = CAM_SIZE_X / IMG_WIDTH
            stepy = CAM_SIZE_Y / IMG_HEIGHT
            alpha = -CAM_SIZE_X * 0.5 + (x + 0.5) * stepx
            beta  = -CAM_SIZE_Y * 0.5 + (y + 0.5) * stepy
        
        elif LOG_IMPACT_CAM:
            stepx = CAM_SIZE_X / IMG_WIDTH
            stepy = CAM_SIZE_Y / IMG_HEIGHT
            r_i = np.exp(np.log(20.) * (x + 0.5)/(IMG_WIDTH)) - 1.
            theta_i = 2.0 * np.pi * (y + 0.5)/ (IMG_HEIGHT)

            alpha = r_i * np.cos(theta_i)
            beta  = r_i * np.sin(theta_i)
# #if (LINEAR_IMPACT_CAM)
        # real stepx = CAM_SIZE_X / (real) IMG_WIDTH;
        # real stepy = CAM_SIZE_Y / (real) IMG_HEIGHT;
        # alpha = -CAM_SIZE_X * 0.5 + (x + 0.5) * stepx;
        # beta  = -CAM_SIZE_Y * 0.5 + (y + 0.5) * stepy;
# #elif (LOG_IMPACT_CAM)
        # real stepx = (real)CAM_SIZE_X / (real) IMG_WIDTH;
        # real stepy = (real)CAM_SIZE_Y / (real) IMG_HEIGHT;
        # real r_i = exp(log(20.)*(real)(x+0.5)/((real)IMG_WIDTH)) - 1.;
        # real theta_i = 2.0*M_PI  * (real)(y+0.5)/((real)IMG_HEIGHT);

        # alpha = r_i * cos(theta_i);
        # beta  = r_i * sin(theta_i);
# #endif
        initialize_photon(alpha, beta, photon_u, t_init)
        # initialize_photon(alpha, beta, photon_u, t_init);

        # // Construct "photon_u"
        X_u[:] = photon_u[:4]
        # LOOP_i {
        #         X_u[i] = photon_u[i];
        # }

# #if (GEOD)
#         fprintf(geod,"%e %e %e\n",X_u[1],X_u[2],X_u[3]);
# #endif

        # // Current r-coordinate
        r_current = np.exp(photon_u[1]) if logscale else photon_u[1]
        # real r_current = logscale ? exp(photon_u[1]) : photon_u[1];
        # // Reset lambda and steps
        lambd = 0.
        # real lambda = 0.;
        steps = 0
        # steps = 0;
        TERMINATE = 0
        # int TERMINATE = 0; // Termination condition for ray

        # // Trace light ray until it reaches the event horizon or the outer
        # // cutoff, or steps > max_steps

# #if ( metric == BL || metric == MBL)
        # // Stop condition for BL coords
        # while (r_current > cutoff_inner && r_current < cutoff_outer &&
        #        steps < max_steps && !TERMINATE) { // && photon_u[0] < t_final){
# #elif (metric == KS || metric == MKS)
        # // Stop condition for KS coords
        # while ( r_current < cutoff_outer && r_current > cutoff_inner &&
        #         steps < max_steps && !TERMINATE) { // 2.26 for Neuton star 3 solar masses
# #endif
        while (r_current > cutoff_inner and r_current < cutoff_outer and steps < max_steps and not TERMINATE): # // && photon_u[0] < t_final){
            # // Current photon position/wave vector
            X_u[:] = photon_u[:4]
            k_u[:] = photon_u[4:]

            # LOOP_i {
            #         X_u[i] = photon_u[i];
            #         k_u[i] = photon_u[i + 4];
            # }

# #if (GEOD)
#                 fprintf(geod,"%e %e %e\n",X_u[1],X_u[2],X_u[3]); //r_current*sin(theta)*cos(X_u[3]),r_current*sin(theta)*sin(X_u[3]),r_current*cos(theta));
# #endif

            # // Possibly terminate ray to eliminate higher order images
            if thetadot_prev * photon_u[6] < 0. and steps > 2:
                    theta_turns += 1
            thetadot_prev = photon_u[6]
            if ((beta < 0. and theta_turns > max_order) or (beta > 0. and theta_turns > (max_order + 1))):
                    TERMINATE = 1

            # if (thetadot_prev * photon_u[6] < 0. && steps > 2)
            #         theta_turns += 1;
            # thetadot_prev = photon_u[6];
            # if((beta < 0. && theta_turns > max_order) || (beta > 0. && theta_turns > (max_order + 1)))
            #         TERMINATE = 1;

            # // Compute adaptive step size
            dlambda_adaptive = stepsize(X_u, k_u)
            # dlambda_adaptive = stepsize(X_u, k_u);

            # // Enter current position/velocity/dlambda into lightpath
            lightpath[:8] = photon_u[:]
            lightpath[8] = np.abs(dlambda_adaptive)
            # for (q = 0; q < 8; q++)
            #         lightpath[ q] = photon_u[q];
            # lightpath[ 8] = fabs(dlambda_adaptive);

            # // Advance ray/particle
            photon_u = rk4_step(photon_u, dlambda_adaptive)
# #if (int_method == RK4)
                # rk4_step(photon_u, dlambda_adaptive);
# #elif (int_method == VER)
#                 verlet_step(photon_u, &f_geodesic, dlambda_adaptive);
# #elif (int_method == RK2)
#                 rk2_step(photon_u, dlambda_adaptive);
# #endif
            X_u[:] = photon_u[:4]
            k_u[:] = photon_u[4:]
            # LOOP_i {
            #         X_u[i] = photon_u[i];
            #         k_u[i] = photon_u[i + 4];
            # }
            
            if X_u[1] > stopx[1] and  k_u[1] < 0:
                break
                    
            # if(X_u[1] > stopx[1] &&  k_u[1] < 0)
            #         break;

            r_current = np.exp(photon_u[1]) if logscale else photon_u[1]
            # r_current = logscale ? exp(photon_u[1]) : photon_u[1];

# #if (RAD_TRANS) # ???? - NO RAD TRANS FOR NOW
#                 if(X_u[1] < stopx[1] && X_u[1] > startx[1] && X_u[2] > startx[2] && X_u[2] < stopx[2])
#                         radiative_transfer(X_u,k_u,lightpath[8], frequencies,icur,intensityfield2,tau,p);
# #endif

            # // Update lambda, r_current, and steps.
            lambd += np.abs(dlambda_adaptive)
            # lambda += fabs(dlambda_adaptive);
            r_current = np.exp(photon_u[1]) if logscale else photon_u[1]
            # r_current = logscale ? exp(photon_u[1]) : photon_u[1];
            steps += 1
            # steps = steps + 1;
# #if (GEOD)
#         fclose(geod);
# #endif
