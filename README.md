#Overview : 

This project presents a numerical simulation of an aircraft landing gear system during touchdown. The landing gear is modeled as a dynamic mass–spring–damper system and solved using a 4th-order Runge–Kutta method to analyze its transient response under impact loading.

The objective is to study:

Vertical compression behavior

Oscillatory damping response

G-load evolution during landing

Structural dynamic behavior under impact

This project demonstrates the application of numerical methods to aerospace structural dynamics problems.

#Physical Model

The landing gear is modeled using Newton’s Second Law:

m x'' + c x' + k x = F(t)

Where:

m – effective mass of aircraft section

c – damping coefficient

k – stiffness of landing gear strut

x(t) – vertical compression

F(t) – external impact force

The governing second-order ODE is converted into a system of first-order equations and solved numerically.
