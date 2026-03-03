#Overview : 


This project presents a numerical simulation of an aircraft landing gear system during touchdown. The landing gear is modeled as a dynamic mass–spring–damper system and solved using a 4th-order Runge–Kutta method to analyze its transient response under impact loading.

-The objective is to study:

-Vertical compression behavior

-Oscillatory damping response

-G-load evolution during landing

-Structural dynamic behavior under impact

----->  This project demonstrates the application of numerical methods to aerospace structural dynamics problems.


#Physical Model :


The landing gear is modeled using Newton’s Second Law:

m x'' + c x' + k x = F(t)

Where:

-m – effective mass of aircraft section

-c – damping coefficient

-k – stiffness of landing gear strut

-x(t) – vertical compression

-F(t) – external impact force

The governing second-order ODE is converted into a system of first-order equations and solved numerically.



#Numerical Method:


The system is integrated using a 4th-order Runge–Kutta (RK4) method for stability and accuracy.

Why RK4?

-High accuracy for nonlinear dynamic systems

-Stable for transient simulations

-Widely used in aerospace and mechanical simulations


#Results :

The simulation produces:

📉 Compression Response

Damped oscillatory motion after touchdown

Peak compression at initial impact

Progressive energy dissipation

📊 G-Load Response

Sharp load variations during rebound phases

Peak acceleration values during impact

Load reversal behavior during oscillation

These outputs allow analysis of landing severity and structural stress behavior.



#Technologies Used :

-Python

-NumPy

-Matplotlib

-Jupyter Notebook

-pytest (unit testing)



#Engineering Significance :


This project demonstrates:

-Application of numerical methods to real engineering systems

-Dynamic system modeling

-Transient response analysis

-Code modularity and test-driven structure

-Integration of computation with mechanical system analysis

-The work reflects the intersection of aerospace engineering and computational simulation.



#Possible Future Improvements :


-Nonlinear damping model

-Tire deformation modeling

-Multi-degree-of-freedom system

-Parametric study on landing velocities

-Energy absorption optimization


#Author :

Developed as part of CS50’s Introduction to Programming with Python, with an aerospace-focused final project applying numerical simulation to mechanical systems.


