# Calculating TOEC from Finite Difference

To calculate TOEC (for cubic only) using these scripts, you need VASP and Python 2.7 with numpy.

Let's say this repo is present in $HOME/TOEC, and your working directory is $HOME/test. In this directory, place an appropriate INCAR, KPOINTS, POTCAR and CONTCAR (not POSCAR) file. Then do <br>

<code>
python $HOME/TOEC/FD/fd.py eta
 </code>
 
 where eta is the step size for finite difference (recommended value of eta is 0.02). This command will create folders for each displacement. VASP should be run in each of the folders. Note that you should not do any relaxation - we only need first principles energy.
 
Once all the calculations are done, do

<code>
  python $HOME/TOEC/FD/cal_constants_FD.py eta volume > Cijk.dat
</code>

where volume is the cell volume. This command will calculate C<sub>111</sub>, C<sub>112</sub>, C<sub>123</sub>, C<sub>144</sub>, C<sub>166</sub>, C<sub>456</sub> and store them in the file Cijk.dat

Note that to keep things simple, this code only calculates the constants that are relevant for cubic symmetry. However, the fd.py script can be very easily modified to add more constants.
