# Calculating Symmetric Wallace Tensor

These scripts and instructions are for uniaxial stretching along z-direction, we will add more functionality later.

To start, you need a file (let's call it Cij.dat) containing the SOEC in 6x6 Voight matrix form. Symmetrize it by using 

<code>
  python $HOME/ElasticToolkit/SWT/symmetrize.py Cij.dat <type>
</code>

Here type refers to the type of symmetrization that needs to be done based on the crystal symmetry. There are 4 available values for type
<ul>
  <li> 1 - tetragonal
  <li> 2 - cubic </li>
  <li> 3 - orthorhombic </li>
  <li> 4 - Voight only </li>
</ul>

This will generate a symmetrized file called Cij_symm.dat. Now before you go any further, ensure that you have the Green-Lagrange strain. This is a different definition of the strain and is more suited to finite deformations, as opposed to the standard engineering strain. To get this, run the following command

<code>
  python $HOME/ElasticToolkit/SWT/get-gl-strain.py <es>
</code>

where es is the engineering strain. For example if you have stretched your system by 5% along z, you will do

<code>
  python $HOME/ElasticToolkit/SWT/get-gl-strain.py 0.05
</code>
The code will print out the corresponding GL strain, which in this case is 0.05125.

Now to get the Piola-Kirchoff 2 (PK2) stress, you need to run the following command

<code>
  python $HOME/ElasticToolkit/SWT/non-cubic-poisson.py <glstrain> <unrelaxed_stretched_POSCAR>
</code>

where <glstrain> is the aforementioned Green-Lagrange strain and <unrelaxed_stretched_POSCAR> refers to the POSCAR file representing the structure which has been stretched along z but not relaxed. Note that you also need the relaxed CONTCAR file present in the same folder. On running this command, the code will print out the relaxed lattice parameters - please verify this by comparing with CONTCAR. It will also generate the deformation gradient and put in a file called F.dat and the PK2 stress, stored in a file called stress.dat

We noe have everything we need to calculate the Wallace tensor.
