# Calculating Symmetric Wallace Tensor

These scripts and instructions are for uniaxial stretching along z-direction, we will add more functionality later.

Here a list of the files you need
<ol>
  <li> A file containing the second order elastic constants in 6x6 Voight matrix form (call it Cij.dat) </li>
  <li> The POSCAR file associated with the uniaxially stretched but unrelaxed (in other directions) structure </li>
  <li> The CONTCAR file associated with the uniaxially stretched and relaxed (in other directions) </li>
  <li> The OUTCAR file obtained after relaxation. The stress tensor will be taken from this file </li>
</ol>
Prepare a folder with these files. First, let's symmetrize the elastic constant matrix by running the following <br>
<br>

```
python $HOME/ElasticToolkit/SWT/symmetrize.py Cij.dat <type>
```
Here type refers to the type of symmetrization that needs to be done based on the crystal symmetry. There are 4 available values for type
<ul>
  <li> 1 - tetragonal
  <li> 2 - cubic </li>
  <li> 3 - orthorhombic </li>
  <li> 4 - Voight only </li>
</ul>

This will generate a symmetrized file called Cij_symm.dat. Now before you go any further, ensure that you have the Green-Lagrange strain. This is a different definition of the strain and is more suited to finite deformations, as opposed to the standard engineering strain. To get this, run the following command

```
python $HOME/ElasticToolkit/SWT/get-gl-strain.py <es>
```

where es is the engineering strain. For example if you have stretched your system by 5% along z, you will do

```
python $HOME/ElasticToolkit/SWT/get-gl-strain.py 0.05
```

The code will print out the corresponding GL strain, which in this case is 0.05125.
Now to get the Piola-Kirchoff 2 (PK2) stress, you need to run the following command

```
python $HOME/ElasticToolkit/SWT/non-cubic-poisson.py <glstrain> <unrelaxed_stretched_POSCAR>
```

where <glstrain> is the aforementioned Green-Lagrange strain and <unrelaxed_stretched_POSCAR> refers to the POSCAR file representing the structure which has been stretched along z but not relaxed. As mentioned at the start, you also need the relaxed CONTCAR file and the OUTCAR file present in the same folder. On running this command, the code will print out the relaxed lattice parameters - please verify this by comparing with CONTCAR. It will also generate the deformation gradient and put it in a file called F.dat. The PK2 stress will be stored in a file called stress.dat

We now have everything we need to calculate the Wallace tensor. To get the wallace tensor, do the following
```
python $HOME/ElasticToolkit/SWT/calculate.py stress.dat Cij_symm.dat
```

The code will print out the symmetrized Wallace tensor, the eigenvalues (in ascending order) and the eigenvectors. Note that the eigenvectors and eigenvalues are in the same order. So the first eigenvalue corresponds to the first eigenvector, and so on. These printed out values can be stored according to your convenience.

Additionally, if there is need to calculate bulk modulus, shear modulus etc, you can easily do that using
```
cat Cij_symm.dat | python $HOME/ElasticToolkit/SWT/VRH.py
```
This will print out the required additional quantities. Note this final optional feature (VRH.py) only works for cubic symmetry.
