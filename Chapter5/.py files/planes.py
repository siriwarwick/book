import plotly.graph_objects as go
import numpy as np

A = np.array([[1,0,-2], [1,-1,1], [2,1,-1]])
b = np.array([1,1,0])

x  = np.linspace(-5,5)
y  = np.linspace(-5,5)
X,Y= np.meshgrid(x,y)
Z1 = (A[0,0]*X + A[0,1]*Y- b[0])/-A[0,2]
Z2 = (A[1,0]*X + A[1,1]*Y- b[1])/-A[1,2]

fig = go.Figure()

plane1 = go.Surface(x=x, y=y, z=Z1, 
                    showscale=False)
plane2 = go.Surface(x=x, y=y, z=Z2, 
                    showscale=False,
                    colorscale='viridis')
 
alpha = np.arange(-2, 2.1, 0.25)
for a in alpha:
    Z3= (A[2,0]*X + a*Y - b[2])/-A[2,2]
    plane3 = go.Surface(x=x, y=y, z=Z3, 
                    showscale=False, 
                    colorscale='blues', 
                    opacity = 0.9,
                    visible=False)
    fig.add_traces([plane1,plane2,plane3])

fig.data[2].visible = True

steps = []

for i, a in enumerate(alpha):
    step = dict(
     method="restyle",
     args=[{"visible":[False]*len(fig.data)}],  
     label=str(a))
    step["args"][0]["visible"][3*i] = True 
    step["args"][0]["visible"][3*i+1] = True 
    step["args"][0]["visible"][3*i+2] = True 
    steps.append(step)

sliders = [dict(steps=steps,              
           currentvalue={"prefix": 'alpha='}, 
           font=dict(size=20))]

fig.update_layout(sliders=sliders, width=700,
    margin=dict(r=20, l=10, b=5, t=5),
    scene = dict(zaxis = dict(range=[-5,5])),
    scene_aspectmode='cube',
    font=dict(size=18))

fig.show(renderer='browser')
