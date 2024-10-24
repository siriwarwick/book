I'll be grateful for notifications of any errors you spotted in the book. Please get in touch via email or using Discussion forum. Your name will be credited (unless you tell me a prefered pseudonym).

## Text errata
p34: "_Newton-Raphson method is discussed in the exercise 11_": remove "the".<br>
p97: "_If you'd like to exclude the part r<0 when using Method I_": change to "when using either method".<br>
p105: Working with tuples: change "_the code above_" to "the code ellipse.ipynb". (Thanks to 夏威 Xia Wei)<br>
p156: Eq 4.15 (RK4) and the line above it. Probably more consistent to write $f(t,y)$ rather than $f(x,y)$. Replace $x_n$ by $t_n$ in the RK4 formula.<br>
p163: Last line of code annotation "_Delay between frames (s)_": change to "Delay between frames (ms)".<br>
p187: Last line of code annotation "_Relabel the ticks on the axes_": move this sentence one line up.<br>
p223: "_The row of A_": change to "The rows of A". (Kit Liu) <br>
p238: "_join the image points again to find the transformed square_": change to "joins the image points again to produce the transformed square".<br>
p304: "_left ledge_" (above table 6.2) : change to "left edge".<br>
p351: Ex 14c(i) "Plot the $\Gamma(x)$": remove "the". Ex 14c(ii) ".. in using the Stirling's": remove "the".<br>
p355: "_the probabilistic number theory_": remove "the".<br>
p365: "_On the right of the same figure_": change to "In the same figure,"<br>
p407: Ex 1c: "_a print out the sums_": change to "a print out of the sums". Should also add that the diagonals are going from bottom left to top right. (Perhaps a figure would be helpful.) <br>
p423: "can in fact be approximated by $N(\mu_\bar{X}, \sigma_\bar{X})$": change $\sigma_\bar{X}$ to $\sigma^2_\bar{X}$ (missing square in the second argument).<br>
On the same page, "Alternatively, we could use the normal approximation $N(0.5, 0.029)$": change $0.029$ to $0.029^2$.<br>
p425: "Equivalently,... approaches $N(\mu_\bar{X}, \sigma_\bar{X})$": change $\sigma_\bar{X}$ to $\sigma^2_\bar{X}$". <br>
p483: Ex 10. The strange symbols "Âč" were meant to be the pound sign £. <br>
p486: Last line. Change "affect" to "affects".

## Code errata

All the following errors have already been corrected in the code on GitHub. They are listed here just for comparison with the book version.<br>

The following were reported by 夏威 Xia Wei.<br>

p2 (continutyslider.ipynb): The line ```y = f(xarray)``` is redundant. <br>


p78 (improper.ipynb): The line which uses Scipy's Simpson's Rule<br>
```integ = simpson(f(x1),x1) + simpson(g(x2),x2)```<br>
will break the code if using Scipy version >1.14. Change this to <br>
```integ = simpson(y=f(x1),x=x1) + simpson(y=g(x2),x=x2)```<br>

p111 (curvature.ipynb). Change<br>
```Pnt1.set_data(rx(t), ry(t))``` to <br>
```Pnt1.set_data([rx(t)], [ry(t)])```<br>
and similarly, change <br>
```Pnt2.set_data(t, kappa(t))``` to <br>
```Pnt2.set_data([t], [kappa(t)])```<br>
This is because in newer versions of matplotlib, the function set_data only takes list arguments. <br>

p347 (zetaanim.ipynb). For the same reason as p111, change<br>
   ```dot1.set_data(Dom_r[i], Dom_i[i])```<br>
  ```dot2.set_data(Img_r[i], Img_i[i])```<br>
to <br>
   ```dot1.set_data([Dom_r[i]], [Dom_i[i]])```<br>
  ```dot2.set_data([Img_r[i]], [Img_i[i]])```<br>
