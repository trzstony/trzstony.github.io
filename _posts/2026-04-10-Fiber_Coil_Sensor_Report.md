---
layout: post
title: "Fiber Coil Sensor Experiment Report"
date: 2026-04-10
---

*Translated and lightly adapted from the original Chinese report.*

## Abstract

In this report, we designed two optical-fiber sensors. The phase-modulation fiber sensor continuously changes the shape of the fiber by means of an extendable spring, measures the resulting change in phase information, and infers the change in spring extension from that optical response. In this way, the sensor enables continuous measurement of several mechanical quantities.

**Keywords:** phase modulation; amplitude modulation; optical fiber sensor

## Background and Objectives

Optical-fiber sensors are a new class of sensors with broad application prospects. They offer strong immunity to electromagnetic interference, good electrical insulation, low weight, and the ability to operate in harsh environments, making them suitable for military, engineering, and power-system applications [1]. When light propagates through an optical fiber, its characteristic parameters, such as amplitude, phase, wavelength, and polarization state, change in response to the physical quantity being measured, such as displacement, temperature, or pressure [2]. By analyzing the modulated optical signal, one can recover the quantity of interest.

Motivated by this principle, the report aims to build low-cost, multifunctional fiber-sensing devices and proposes two designs: a phase-modulation sensor and an amplitude-modulation sensor.

The phase-modulation fiber sensor works by modulating the phase information of the light in the fiber and measuring the change in the polarization state of the output beam. The experiment tests the theoretical prediction that the geometric torsion of the fiber changes the direction of polarization. Based on that effect, the team builds a fiber-coil sensor capable of continuous measurement of multiple mechanical quantities. In practice, the device changes the fiber geometry continuously by stretching a spring, which makes it suitable for continuous measurement and for applications such as real-time monitoring of bridge structures. Its main advantages are low cost and high resolution.

More broadly, the coil sensor proposed in the report is inexpensive and can be adapted to measure several physical quantities. By redesigning the fiber coil for specific needs, it can achieve high resolution, high sensitivity, and high flexibility, while allowing the measurement function and range to be changed quickly in response to practical requirements.

## Experimental Principle

### 1. Change in Polarization Direction

Using classical electromagnetic theory together with differential geometry, the report derives the general relation between the polarization direction and the solid angle traced in momentum space. Consider an ideal single-mode fiber placed as a space curve in three dimensions. Using the arc length of the fiber as the curve parameter, one introduces the Frenet frame: the unit tangent vector points along the direction of light propagation, together with the principal normal and binormal vectors. The Frenet formulas describe how this moving frame changes along the fiber.

$$
\frac{d}{ds}
\begin{pmatrix}
\mathbf{t} \\
\mathbf{n} \\
\mathbf{b}
\end{pmatrix}
=
\begin{pmatrix}
0 & \kappa & 0 \\
-\kappa & 0 & \tau \\
0 & -\tau & 0
\end{pmatrix}
\begin{pmatrix}
\mathbf{t} \\
\mathbf{n} \\
\mathbf{b}
\end{pmatrix}.
$$

![Figure 1. Frenet frame of the optical fiber.](/assets/images/fiber-coil-sensor-report/figure-1-frenet-frame.png)

**Figure 1.** Frenet frame of the optical fiber.

At any point on the fiber, consider a linearly polarized wave whose electric-field direction makes an angle $\theta$ with the local frame. Over a small propagation distance, the electric-field direction remains fixed in space, but the local normal direction rotates because the curve has torsion. As a result, the angle describing the polarization direction changes slightly. Integrating that infinitesimal change along the fiber gives the accumulated polarization rotation:

$$
\theta(l)=\theta_0-\int_0^l \tau(s)\,ds.
$$

Now consider the unit tangent vector traced on the unit sphere. The report calls this spherical curve the tangent indicatrix. If the tangent direction at the end of the fiber matches that at the beginning, then this curve closes on the sphere.

![Figure 2(a). Wave vector inside the fiber.](/assets/images/fiber-coil-sensor-report/figure-2a-wave-vector-in-fiber.png)

![Figure 2(b). Tangent indicatrix traced by the wave vector on the unit sphere.](/assets/images/fiber-coil-sensor-report/figure-2b-tangent-indicatrix.png)

**Figure 2.** Wave vector and tangent indicatrix in the general case.

Because the curve lies on the unit sphere, the solid angle enclosed by the tangent indicatrix equals the spherical area it bounds. The report uses the Gauss-Bonnet theorem to relate that enclosed solid angle to the accumulated polarization change:

$$
\iint K\,dA+\oint \kappa_g\,ds'=2\pi.
$$

In the present setting,

$$
\kappa_g=\frac{d\mathbf{s}'}{ds'}\cdot(\mathbf{n}\times\mathbf{b}),
\qquad
\frac{d\mathbf{n}}{ds}=-\kappa \mathbf{t}+\tau \mathbf{b},
\qquad
\kappa_g\,ds'=\tau\,ds.
$$

Since the Gaussian curvature of the unit sphere is $K=1$, the enclosed solid angle is

$$
\Omega=\iint K\,dA.
$$

To simplify the experiment, the fiber is wound into a cylindrical helix.

![Figure 3(a). Wave vector for a helical fiber geometry.](/assets/images/fiber-coil-sensor-report/figure-3a-helical-wave-vector.png)

![Figure 3(b). Tangent indicatrix of the helical case on the unit sphere.](/assets/images/fiber-coil-sensor-report/figure-3b-helical-tangent-indicatrix.png)

**Figure 3.** Wave vector and tangent indicatrix in the helical special case.

In this geometry, the solid angle traced by the wave vector in momentum space can be computed directly from the helix parameters:

$$
\Omega = 2\pi(1-\cos\alpha),
\qquad
\tan\alpha=\frac{\pi D}{l},
\qquad
\cos\alpha=\frac{1}{\sqrt{1+\tan^2\alpha}}.
$$

Therefore, after one pitch the polarization rotation is

$$
\Delta \phi_0
=
2\pi\left(1-\frac{1}{\sqrt{1+\left(\frac{\pi D}{l}\right)^2}}\right),
$$

and for the five-turn spring used in the experiment,

$$
\Delta \phi
=
5\cdot 2\pi\left(1-\frac{1}{\sqrt{1+\left(\frac{\pi D}{l}\right)^2}}\right).
$$

Therefore, by measuring the change in the polarization direction of the output laser beam, one can infer the change in the fiber shape. The report further explains that when the cylindrical diameter and pitch of the helix are known, the polarization rotation after one pitch and after multiple turns can be related to the phase change of the light. In the actual setup the spring contains five turns, and over the experimental range the relation between polarization rotation and spring length is approximately linear. This linear regime is what makes continuous sensing feasible.

### 2. Measurement Principle

An ideal linearly polarized wave oscillates in only one fixed direction transverse to the direction of propagation. After the beam passes through a polarizer, only the component aligned with the transmission axis is transmitted, so the output intensity is generally lower than the incident intensity.

Using Malus's law, the transmitted intensity can be written as a function of the analyzer angle $\theta$ and the polarization direction $\phi$ of the light emerging from the fiber:

$$
I=I_0\cos^2(\theta-\phi).
$$

The fitted maxima satisfy

$$
\theta-\phi=n\pi,\qquad n=0,1,2,\ldots
$$

so one may take the effective range

$$
\phi\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right)
$$

to remove the integer-multiple ambiguity. In the experiment, the analyzer in front of the power meter is rotated in steps of 15 degrees, and the optical power is recorded at each angle. Plotting these data produces a scatter plot that is approximately sinusoidal. The angle corresponding to the maximum of the fitted curve gives the polarization direction of the output beam. By comparing the fitted curves for different spring lengths, one can recover how the output polarization direction changes with the elongation of the spring.

## Experimental Apparatus

### 1. Overview of the Optical Setup

The phase-modulation experiment is shown below.

![Figure 5. Experimental setup of the phase-modulation optical-fiber sensor.](/assets/images/fiber-coil-sensor-report/figure-5-experimental-setup.png)

**Figure 5.** Experimental setup of the phase-modulation optical-fiber sensor.

The laser is first coupled into the optical fiber. A polarizer is inserted to ensure that the incident light is linearly polarized. An analyzer is then placed between the fiber-output collimator and the optical power meter so that changes in polarization direction can be detected.

### 2. Fiber-Shape Adjustment and Phase-Modulation System

The mechanical subsystem that changes the fiber geometry is shown in Figure 6. The fiber is fixed onto the spring by multiple sections of Teflon tubing in order to reduce friction. The spring is attached to a steel support, with its front end fixed and its rear end free to slide. A long screw runs through the support and is used to control the spring length.

![Figure 6. Fiber-shape adjustment and phase-modulation system.](/assets/images/fiber-coil-sensor-report/figure-6-phase-modulation-system.jpeg)

**Figure 6.** Fiber-shape adjustment and phase-modulation system.

The key innovation of the device is that stretching or compressing the spring continuously changes the shape of the fiber and therefore continuously changes the polarization direction of the transmitted light. By recording the analyzer angle and the power-meter reading, the experiment extracts the change in polarization direction.

## Experimental Procedure

1. Assemble the optical path shown in Figure 5 and adjust the laser coupler so that the laser is fully coupled into the fiber.
2. Because the laser source itself has some intrinsic polarization, adjust the input polarizer so that the optical power at the fiber output is maximized.
3. Rotate the analyzer and observe the power-meter reading. Record one pair of analyzer angle and power value every 15 degrees.
4. Adjust the spring length and record it. The spring is extended by 1 cm each time, for a total of six datasets. For each dataset, fit the measured intensity values with a trigonometric function and use the phase of the fitted curve to determine the polarization direction of the linearly polarized light emerging from the fiber.

## Experimental Data and Data Processing

### Table 1. Parameters Used in the First Part of the Experiment

| Spring length `h` | Spring diameter `d` | Fiber diameter | Fiber length | Core diameter |
| --- | --- | --- | --- | --- |
| 120.0 mm | 50.0 mm | 3.0 mm | 1.00 m | 9.0 um |

### Table 2. Phase-Modulation Fiber Sensor Data

| Analyzer angle (deg) | `h = 6.50 cm` | `h = 7.50 cm` | `h = 8.50 cm` | `h = 9.50 cm` | `h = 10.50 cm` | `h = 11.50 cm` |
| --- | --- | --- | --- | --- | --- | --- |
| 0.0 | 16 | 23 | 46 | 63 | 63 | 56 |
| 15.0 | 20 | 29 | 55 | 75 | 71 | 59 |
| 30.0 | 30 | 33 | 61 | 80 | 72 | 59 |
| 45.0 | 34 | 36 | 65 | 81 | 68 | 56 |
| 60.0 | 41 | 38 | 64 | 70 | 59 | 49 |
| 75.0 | 44 | 37 | 59 | 56 | 45 | 41 |
| 90.0 | 42 | 34 | 52 | 41 | 34 | 33 |
| 105.0 | 40 | 29 | 45 | 29 | 26 | 29 |
| 120.0 | 33 | 25 | 38 | 23 | 25 | 30 |
| 135.0 | 24 | 21 | 35 | 26 | 29 | 34 |
| 150.0 | 19 | 19 | 35 | 35 | 38 | 42 |
| 165.0 | 16 | 20 | 40 | 48 | 54 | 52 |
| 180.0 | 17 | 24 | 48 | 64 | 63 | 59 |

The data in Table 2 are plotted as scatter points and fitted with a trigonometric function to obtain the relationship between intensity and analyzer angle.

![Figure 7. Optical intensity as a function of analyzer angle.](/assets/images/fiber-coil-sensor-report/figure-7-intensity-vs-analyzer-angle.png)

**Figure 7.** Optical intensity versus analyzer angle.

As the spring length changes, the solid angle described by the wave vector changes continuously. The report compares the measured polarization direction inferred from the fits with the theoretical prediction for the dependence of output polarization direction on spring length.

![Figure 8. Relationship between output polarization direction and spring length.](/assets/images/fiber-coil-sensor-report/figure-8-polarization-vs-spring-length.jpeg)

**Figure 8.** Output polarization direction as a function of spring length.

Figure 8 shows that the angle through which the polarization direction rotates after transmission through the fiber depends approximately linearly on the spring length. A linear fit to the experimental data agrees with the theoretical prediction, with slope

$$
0.392\ \text{rad/cm}.
$$

Therefore, for each additional `1 cm` of extension, the output polarization direction increases by approximately

$$
0.392\ \text{rad}\approx 22.47^\circ.
$$

This demonstrates that the device can continuously encode displacement into phase and polarization information.

Using the relation derived earlier between polarization rotation and optical phase, the phase information of the polarized light can be inferred from these data. Experimentally, as the spring is stretched from a shorter state to a longer one, the polarization direction changes continuously, monotonically, and with good linearity. In practical sensing applications, this makes it possible to infer changes in spring length, displacement, or force by measuring the phase or polarization shift after calibration. The report highlights real-time structural monitoring of bridges as one representative application.

## Conclusion and Outlook

The report proposes a new multifunctional fiber-coil sensor and offers a useful design idea for other optical-fiber sensors. First, the experiment verifies the theoretical relationship between fiber geometric torsion and the change in polarization direction, and then uses that effect to modulate the optical phase, producing a sensor capable of measuring force, displacement, velocity, acceleration, and related mechanical quantities. Second, the broader project also considers amplitude modulation using a bare multimode fiber coil for sensing quantities such as liquid concentration and water level.

Compared with earlier sensors based on similar ideas or with similar functions, the group argues that its design has several practical strengths: a simple model, convenient operation, the ability to measure multiple physical quantities, adaptability to different measurement conditions, and a tunable measurement range. Because both experiments rely on fiber coils, the report concludes that it is feasible to build a low-cost, multifunctional fiber-sensing device with high resolution and high sensitivity that can also operate in moderately harsh environments.

The report also emphasizes that many of these measurement functions can be implemented on the same fiber by changing the fiber type, winding diameter, or number of turns. This gives the device a high degree of integration and makes it suitable for both industrial production and civilian equipment.

## Work Summary

Under the guidance of the supervising instructor, the team completed the following main tasks:

1. Designed the fiber-shape adjustment and phase-modulation system independently.
2. Performed the experiment, collected data, and processed and fitted the results with custom code.
3. Used the apparatus to measure multiple physical quantities and successfully demonstrate the sensing concept.

## References

1. 丁小平,王薇,付连春.光纤传感器的分类及其应用原理[J].光谱学与光谱分析,2006(06):1176-1178.
2. 侯俊芳,裴丽,李卓轩,刘超.光纤传感技术的研究进展及应用[J].光电技术应用,2012,27(01):49-53.
3. 彭家贵，陈卿. 微分几何. 第2版[M]. 高等教育出版社, 2021.22-23.
4. R. Ulrich and A. Simon, Appl. Opt. 18, 2241 (1979)
5. 邢进华.用光纤迈克尔逊干涉仪测量晶体的弹光系数[J].常熟理工学院学报,2005(06):27-30.
6. 李长胜,陈佳.去除光学器件弹光双折射的方法[J].物理学报,2016,65(03):298-305.
7. 赵凯华, 钟锡华. 光学[M]. 北京大学出版社; 1984.
8. 张志伟，尹卫峰，温廷敦，朱林泉，张记龙. 溶液浓度与其折射率关系的理论和实验研究[J]. 中北大学学报. 2009(30.03).
9. 张娜. 光纤传感器液体浓度检测系统的研究[D].山东大学,2005.
10. 杨建春,徐龙君,章鹏.倏逝波型光纤气体传感器研究进展[J].光学技术,2008(04):562-567.
11. 王敏,戴世勋,张培晴,王训四,康世亮,刘自军.基于中红外光纤的倏逝波传感研究进展[J].
12. 邹林森 ,张滨.多模光纤微弯和弯曲损耗的实验研究[J].光通信研究,1984(04):42-49.
13. 刘叶新,杨晓云,陈学琴,邓莉,傅思镜,林位株.多模光纤弯曲损耗的分析[J].中山大学学报(自然科学版),2002(05):25-27.
14. 何国财. 多模光纤的弯曲损耗实验研究[D]. 吉首大学,2011.

## Device and Cost

For the phase-modulation optical-fiber sensor, the apparatus used a semiconductor laser, polarizers, a free-space fiber coupler, a fiber-output collimator, a laser power indicator, and the custom-built fiber-shape adjustment and phase-modulation system. That mechanical system was made from a `1 m` single-mode fiber patch cord, a `50 cm` steel tube with `15 mm` inner diameter, two sets of `M6 x 150` stainless-steel screws, and a custom spring of size `50 mm x 120 mm`.

According to the report, the `1 m` single-mode patch cord cost `4 yuan`, the stainless-steel screws cost `8 yuan`, and the custom spring cost `16 yuan`. The remaining components were laboratory instruments. The total cost of the self-built mechanical subsystem was therefore about `50 yuan`.

![Photo of the phase-modulation optical-fiber sensing device.](/assets/images/fiber-coil-sensor-report/device-photo.png)

**Figure 14.** Photo of the phase-modulation optical-fiber sensing device.
