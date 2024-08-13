---
title: '`Cthulhu`: An Open Source Molecular and Atomic Cross Section Computation Code for Substellar Atmospheres'
tags:
  - Python
  - astronomy
  - exoplanets
  - cross sections
  - line lists
  - opacities
  - spectroscopy
  - JWST
authors:
  - name: Arnav Agrawal
    orcid: 0000-0003-2944-0600
    affiliation: "1, 2"
  - name: Ryan J. MacDonald
    orcid: 0000-0003-4816-3469
    affiliation: "3, 4, 2"
affiliations:
  - name: Johns Hopkins University Applied Physics Laboratory, 11100 Johns Hopkins Rd., Laurel, MD 20723, USA
    index: 1
  - name: Department of Astronomy and Carl Sagan Institute, Cornell University, 122 Sciences Drive, Ithaca, NY 14853, USA
    index: 2
  - name: Department of Astronomy, University of Michigan, 1085 S. University Ave., Ann Arbor, MI 48109, USA
    index: 3
  - name: NHFP Sagan Fellow
    index: 4

date:
bibliography: paper.bib

--- 

# Summary

Atmospheric studies of exoplanets and brown dwarfs are a cutting-edge and rapidly evolving area of astrophysics research. Powerful new telescopes, such as the James Webb Space Telescope (JWST) [@Gardner:2023] and the upcoming Extremely Large Telescopes [@Skidmore:2015; @Fanson:2022; @Padovani:2023], are able to capture in detail spectra of planets and brown dwarfs and thereby probe their chemical composition and physical properties. Calculating models of exoplanet or brown dwarf spectra requires knowledge of the wavelength-dependent absorption of light (cross sections) by the molecules and atoms in the atmosphere [@Seager:2010; @Heng:2017]. Reliably calculating spectra of substellar atmospheres requires accurate cross sections, without which measurements of chemical abundances and other atmospheric properties can be biased [e.g., @Anisman:2022; @Hedges:2016; @Gharib-Nezhad:2019]. 

Cross sections are typically pre-computed on a grid of pressures and temperatures from large databases of quantum mechanical transitions (line lists), such as ExoMol [@Tennyson:2020], HITRAN [@Gordon:2022], HITEMP [@Rothman:2010], and VALD [@Pakhomov:2017]. However, calculating cross sections from line lists is often computationally demanding and has required complex and specialised tools. We aim here to lower the access barrier for users to learn how to calculate molecular and atomic cross sections. 

`Cthulhu` is a fully Python package that rapidly calculates cross sections from atomic and molecular line lists. `Cthulhu` includes modules to automatically download molecular line lists from online databases and compute cross sections on a user-specified temperature, pressure, and wavenumber grid. `Cthulhu` requires only CPUs and can run on a user's laptop (for smaller line lists with < 100 million lines) or on a large cluster in parallel (for many billion lines). `Cthulhu` includes in-depth Jupyter tutorials in the online documentation. Finally, `Cthulhu` is intended not only for research purposes, but as an educational tool to demystify the process of making cross sections for atmospheric models.

# Statement of Need

JWST has recently significantly expanded the number of exoplanet and brown dwarfs with high-quality spectra spanning a wide wavelength range [e.g., @Beiler:2023; @Miles:2023; @Carter:2024; @Welbanks:2024]. High-fidelity spectra motivate detailed intercomparisons of exoplanet and brown dwarf modeling codes [e.g. @Barstow:2020], which often identify opacity database differences as a key modelling limitation. Ground-based high spectral resolution datasets [e.g., @Birkby:2017; @Snellen:2010; @Pelletier:2023] also critically rely on up-to-date opacity data, since older inaccurate line lists can lead to non-detections of molecules via cross correlations [e.g. @Merritt:2020] and propagate into retrieved chemical abundances [e.g. @Brogi:2019]. However, despite the key need to continually refine exoplanet and brown dwarf models with the latest state-of-the-art opacities, the process of calculating molecular and atomic cross sections is a non-trivial task that is typically outside the speciality of many exoplanet and brown dwarf researchers.

We have built `Cthulhu` to provide a user-friendly tool for beginners to learn how to work with the most commonly used line list databases and to readily calculate molecular and atomic cross sections. There are other open source codes that can calculate cross sections, such as HELIOS-K [@Grimm:2015; @Grimm:2021] and ExoCross [@Yurchenko:2018], that offer impressive computational performance and are excellent tools for experts to calculate cross sections. However, HELIOS-K requires Nvidia GPUs to run while ExoCross is built in Fortran, both of which can pose accessibility issues for beginners. We offer `Cthulhu`, a fully Python code designed to run on CPUs, as a user-friendly entry point into the world of cross sections for substellar atmospheres.

# Computing Molecular and Atomic Cross Sections with `Cthulhu`

The purpose of the `Cthulhu` package is schematically represented in \autoref{fig:Cthulhu_architecture}. Here we walk through this flowchart, highlighting major use cases of `Cthulhu` and the package's role in the broader process of modelling exoplanetary and brown dwarf atmospheres.

![The role and applications of the `Cthulhu` Python package. `Cthulhu` can download molecular and atomic line lists and calculate the corresponding absorption cross sections as a function of temperature, pressure, and wavenumber. Cross sections made by `Cthulhu` can be used in radiative transfer codes to calculate model spectra of exoplanet and brown dwarf atmospheres. \label{fig:Cthulhu_architecture}](figures/Cthulhu_JOSS_Figure.png){width=100%}

The first use of `Cthulhu` is to download existing molecular line lists from online databases. `Cthulhu`'s `summon` function can automatically download lines lists from ExoMol and HITRAN/HITEMP and reformat the line lists into space-efficient HDF5 files. Ancillary input files required to calculate cross sections, such as partition functions and pressure broadening files, are also downloaded automatically. Alternatively, the user may manually download a line list from their respective websites and point `Cthulhu` to the directory hosting the files. VALD line lists must be downloaded manually by a user with an account on [http://vald.astro.uu.se/](http://vald.astro.uu.se/) (given the terms of use for VALD3), but we provide instructions on how to do this in the `Cthulhu` documentation. `Cthulhu` currently supports ExoMol, HITRAN, HITEMP, and VALD line lists, though we welcome user requests for additional line list databases support. Once a line list has been downloaded, the user can move onto the next major use case of `Cthulhu`, computing cross sections.

The foremost feature of `Cthulhu` is its ability to straightforwardly compute atomic and molecular cross sections at high speeds (typically > 100,000 lines per second on one CPU). `Cthulhu` calculates cross sections via a generalisation of the Vectorised Voigt method [@Yurchenko:2018], whereby complex derivatives are used to perturb a grid of pre-computed template Voigt profiles to the specific properties of each given line [see @MacDonald:2019 for the mathematical description of the underlying algorithm]. `Cthulhu` is accessible, as it does not require GPUs, can run on a standard laptop, and as a fully Python code it is easy for beginners to install and use. To compute a cross section, a user simply calls `Cthulhu`'s `compute_cross_section` function, specifying the location of the line list, the temperature and pressure, and the wavenumber range. More advanced users can specify custom settings via optional arguments (e.g. Voigt wing cutoffs, intensity cutoffs, or a user-provided pressure broadening file). The documentation and function doc strings explain the various arguments users can provide to `compute_cross_section`. The computed cross section is output by default as a .txt file in the `output` folder on the user's machine, which can be readily used to create an opacity database in a user-preferred format for a specific radiative transfer code. `Cthulhu` also offers utility functions to combine multiple cross section .txt files (e.g. a grid of cross sections for different temperature and pressures for one or more chemical species) into an HDF5 cross section database, as illustrated in our [`quick start`](https://cthulhu.readthedocs.io/en/latest/content/quick_start.html) guide.

\autoref{fig:Cthulhu_architecture} illustrates three example applications of `Cthulhu`: (i) molecular cross section calculations for common opacity sources in hot giant exoplanets; (ii) atomic and ionic cross sections, including sub-Voigt wings for the Na and K resonance doublets; and (iii) cross sections for different isotopologues of the same molecule.

The cross section database HDF5 files produced by `Cthulhu` can be readily adapted for the user's favourite exoplanet or brown dwarf modeling or retrieval code. Cross section HDF5 files calculated by `Cthulhu` are already being used in the `POSEIDON` retrieval code [@MacDonald:2023] and other retrieval codes will be supported soon. The lower part of \autoref{fig:Cthulhu_architecture} illustrates one such application, namely the calculation of exoplanet transmission spectra, for which `Cthulhu`'s cross sections can be used an input to an exoplanet spectrum model. Exoplanet transmission spectra modelling codes use cross sections to solve the equation of radiative transfer [e.g. @MacDonald:2022] by calculating the slant optical depth (the integral of the extinction coefficient along the line of sight, e.g. @Fortney:2005) for many rays of light passing through the exoplanet atmosphere. The final output of such a transmission spectrum calculation is the effective planet-star area ratio (i.e. transit depth) as a function of wavelength seen by a distant observer. Cross sections are similarly used to calculate the attenuation of light along the path of a ray in other observing geometries (e.g. secondary eclipses of exoplanets or directly imaged brown dwarfs).

# Future Developments

`Cthulhu` v1.0 supports line lists from the commonly used ExoMol, HITRAN, HITEMP, and VALD databases, but support for other databases (e.g. Kurucz) can be added in the future. `Cthulhu` currently uses Voigt profiles by default (with the exception of the strong Na and K resonance features), but more complex line profiles (e.g. speed-dependent Voigt) are under consideration for future releases. We will shortly add additional HDF5 packaging functions to generate out-of-the-box the opacity formats used by other open source exoplanet and brown dwarf retrieval codes, including petitRADTRANS [@Molliere:2019], TauREx [@Waldmann:2015], CHIMERA [@Line:2013], and Brewster [@Burningham:2017]. Suggestions for additional features are more than welcome and the easiest way is by [`opening an issue`](https://github.com/MartianColonist/Cthulhu/issues) on GitHub. To contribute directly to `Cthulhu`, please see our [`contribution guidelines`](https://cthulhu.readthedocs.io/en/latest/content/contributing.html).

# Documentation

Documentation for `Cthulhu`, with a quick start guide and step-by-step tutorials, is available at [https://cthulhu.readthedocs.io/en/latest/](https://cthulhu.readthedocs.io/en/latest/). 

# Similar Tools

[`HELIOS-K`](https://github.com/exoclime/HELIOS-K) [@Grimm:2015; @Grimm:2021], [`ExoCross`](https://github.com/Trovemaster/exocross) [@Yurchenko:2018], [`RADIS`](https://github.com/radis/radis) [@Pannier:2019], [`PyExoCross`](https://github.com/Beryl-Jingxin/PyExoCross) [@Zhang:2024]

# Acknowledgements

RJM acknowledges support from NASA through the NASA Hubble Fellowship grant HST-HF2-51513.001 awarded by the Space Telescope Science Institute, which is operated by the Association of Universities for Research in Astronomy, Inc., for NASA, under contract NAS5-26555. RJM thanks Sergei Yurchenko, Mark Marley, Natasha Batalha, Ehsan Gharib-Nezhad, Robert Hargreaves, and Iouli Gordon for helpful discussions on line lists, opacities, and cross section computation techniques.

# References