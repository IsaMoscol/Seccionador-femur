# -*- coding: utf-8 -*-
import streamlit as st

st.title("Secciones Fémur")

file = st.file_uploader("File Uploader-Coordenadas", type='csv')
if file is not None:
  df = pd.read_csv(file, encoding = "ISO-8859-1", delimiter='|')
  if st.checkbox('Ver los archivos'):
    st.write(df)

a = df.values
a[:,0:1]

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs

"""Hierarchical Linkage"""

from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters=6, affinity='euclidean', linkage='single') # euclidean: distance between the datapoints
cluster.fit_predict(a) #fit_predict: returns the names of the clusters that each data point belongs to

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(a[:,0],a[:,1], a[:,2], c=cluster.labels_, cmap='rainbow', edgecolor='k', s=40, alpha=0.5)

ax.set_title("Groups")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.dist = 10

df['cluster']= cluster.labels_
print(df)

#Assign groups
group_1 = df[df['cluster'] == 0]
group_2 = df[df['cluster'] == 1]
group_3 = df[df['cluster'] == 2]
group_4 = df[df['cluster'] == 3]
group_5 = df[df['cluster'] == 4]
group_6 = df[df['cluster'] == 5]

print(max(cluster.labels_))

"""# Group 1"""

g1 = group_1.values
g1[:,0:1]

kmeans1 = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=1)
pred_y1 = kmeans1.fit_predict(g1)

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(g1[:,0],g1[:,1],g1[:,2], 
            c=pred_y1, cmap='viridis',
            edgecolor='k', s=40, alpha = 0.5)


ax.set_title("g1")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.dist = 10

ax.scatter(kmeans1.cluster_centers_[:,0], kmeans1.cluster_centers_[:,1], 
           kmeans1.cluster_centers_[:,2], 
           s = 300, c = 'r', marker='*', label = 'Centroid')

plt.autoscale(enable=True, axis='x', tight=True)    

plt.show()

kmeans1.cluster_centers_

"""# Group 2"""

g2 = group_2.values
g2[:,0:1]
my_centroids = np.array([[-30, 0, 0, 1, 1], [0, 0, 0, 1, 2], [-10, -20, 0, 1, 3], [-10, 20, 0, 1, 3]])
kmeans2 = KMeans(n_clusters=4, init=my_centroids, max_iter=300, n_init=10, random_state=0)
pred_y2 = kmeans2.fit_predict(g2)

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(g2[:,0],g2[:,1],g2[:,2], 
            c=pred_y2, cmap='viridis',
            edgecolor='k', s=40, alpha = 0.5)

ax.set_title("g2")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.dist = 10

ax.scatter(kmeans2.cluster_centers_[:,0], kmeans2.cluster_centers_[:,1], 
           kmeans2.cluster_centers_[:,2], 
           s = 300, c = 'r', marker='*', label = 'Centroid')

plt.autoscale(enable=True, axis='x', tight=True)    

st.pyplot(fig)

kmeans2.cluster_centers_

"""# Group 3"""

g3 = group_3.values
g3[:,0:1]
my_centroids = np.array([[-30, 0, 0, 1, 1], [0, 0, 0, 1, 2], [-10, -20, 0, 1, 3], [-10, 20, 0, 1, 3]])

kmeans3 = KMeans(n_clusters=4, init=my_centroids, max_iter=300, n_init=10, random_state=0)
pred_y3 = kmeans3.fit_predict(g3)

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(g3[:,0],g3[:,1],g3[:,2], 
            c=pred_y3, cmap='viridis',
            edgecolor='k', s=40, alpha = 0.5)


ax.set_title("g3")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.dist = 10

ax.scatter(kmeans3.cluster_centers_[:,0], kmeans3.cluster_centers_[:,1], 
           kmeans3.cluster_centers_[:,2], 
           s = 300, c = 'r', marker='*', label = 'Centroid')

plt.autoscale(enable=True, axis='x', tight=True)    

st.pyplot(fig)

kmeans3.cluster_centers_

"""# Group 4"""

g4 = group_4.values
g4[:,0:1]

np.random.seed(1)
kmeans4 = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=1)
pred_y4 = kmeans4.fit_predict(g4)

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(g4[:,0],g4[:,1],g4[:,2], 
            c=pred_y4, cmap='viridis',
            edgecolor='k', s=40, alpha = 0.5)


ax.set_title("g4")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.dist = 10

ax.scatter(kmeans4.cluster_centers_[:,0], kmeans4.cluster_centers_[:,1], 
           kmeans4.cluster_centers_[:,2], 
           s = 300, c = 'r', marker='*', label = 'Centroid')

plt.autoscale(enable=True, axis='x', tight=True)    

st.pyplot(fig)

kmeans4.cluster_centers_

"""# Group 5"""

g5 = group_5.values
g5[:,0:1]

np.random.seed(1)
kmeans5 = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y5 = kmeans5.fit_predict(g5)

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(g5[:,0],g5[:,1],g5[:,2], 
            c=pred_y5, cmap='viridis',
            edgecolor='k', s=40, alpha = 0.5)


ax.set_title("g5")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.dist = 10

ax.scatter(kmeans5.cluster_centers_[:,0], kmeans5.cluster_centers_[:,1], 
           kmeans5.cluster_centers_[:,2], 
           s = 300, c = 'r', marker='*', label = 'Centroid')

plt.autoscale(enable=True, axis='x', tight=True)    

st.pyplot(fig)

kmeans5.cluster_centers_

"""# Group 6"""

g6 = group_6.values
g6[:,0:1]

kmeans6 = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y6 = kmeans6.fit_predict(g6)

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(g6[:,0],g6[:,1],g6[:,2], 
            c=pred_y6, cmap='viridis',
            edgecolor='k', s=40, alpha = 0.5)


ax.set_title("g6")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.dist = 10

ax.scatter(kmeans6.cluster_centers_[:,0], kmeans6.cluster_centers_[:,1], 
           kmeans6.cluster_centers_[:,2], 
           s = 300, c = 'r', marker='*', label = 'Centroid')

plt.autoscale(enable=True, axis='x', tight=True)    

st.pyplot(fig)

kmeans6.cluster_centers_

"""# Todos"""

df.loc[df.cluster == 0,"zone"] = pred_y1
df.loc[df.cluster == 1,"zone"] = pred_y2
df.loc[df.cluster == 2,"zone"] = pred_y3
df.loc[df.cluster == 3,"zone"] = pred_y4
df.loc[df.cluster == 4,"zone"] = pred_y5
df.loc[df.cluster == 5,"zone"] = pred_y6


import math
import base64

"""**Grupo 1**"""

df1 = []
data = df.values
df11 = []

for h in range(0,6,1):

  points = []
  points_test = []

  # Almacenar los puntos del grupo 1
  for w in range(0,len(data),1):
      if data[w,4] == h:
        points.append([data[w,0], data[w,1], data[w,2], data[w,3], data[w,4], data[w,5]])

  points = np.array(points)

  # Cluster centers
  if points[1,4] == 0:
    kmeansx = kmeans1.cluster_centers_
  elif points[1,4] == 1:
    kmeansx = kmeans2.cluster_centers_
  elif points[1,4] == 2:
    kmeansx = kmeans3.cluster_centers_
  elif points[1,4] == 3:
    kmeansx = kmeans4.cluster_centers_
  elif points[1,4] == 4:
    kmeansx = kmeans5.cluster_centers_
  elif points[1,4] == 5:
    kmeansx = kmeans6.cluster_centers_

  #Seleccion de puntos de referencia
  backup = []

  for i in range(0,4,1):
      for j in range(0,len(points),1):   
        d = math.sqrt((kmeansx[i,0]-points[j,0])**2 + (kmeansx[i,1]-points[j,1])**2 + (kmeansx[i,2]-points[j,2])**2) #distancia a kmeans
        backup.append([points[j,0], points[j,1], points[j,2], points[j,3], points[j,4], points[j,5], d]) # guardo las distancias y sus valores
      backup = np.array(backup)
      posicion = np.where( backup[:,6] == np.amin(backup[:,6]) ) # distancia mínima
      points_test.append([backup[posicion[0][0],0], backup[posicion[0][0],1], backup[posicion[0][0],2], backup[posicion[0][0],3],
                        backup[posicion[0][0],4], backup[posicion[0][0],5]])
      backup = []

  points_test = np.array(points_test)
  points_test = pd.DataFrame(points_test)
  #Ordenar los puntos de referencia en funcion de x
  points_test = points_test.sort_values(0)
  points_test = np.array(points_test)

  ###

  ref11 = []
  ref22 = []
  ref33 = []
  ref44 = []

  #Elegir el valor con menor x
  for i in range(0,len(points_test)-2,1):
    if points_test[i,0] < points_test[i+1,0]:
      # Comparar su valor en y con el resto
      for j in range(0,len(points_test)-2,1):
        if points_test[i,1] < points_test[j,1]:
          #zona 0
          ref11 = []
          ref11.append([points_test[i,0],points_test[i,1],points_test[i,2],points_test[i,3],points_test[i,4],points_test[i,5]])
        else:
          #zona 3
          ref44 = []
          ref44.append([points_test[i,0],points_test[i,1],points_test[i,2],points_test[i,3],points_test[i,4],points_test[i,5]])
  
  ref11 = np.array(ref11)
  ref44 = np.array(ref44)

  #drop
  for p in range(0,len(points_test),1):
    if points_test[p,0] == ref11[0,0]:
      test_del = np.delete(points_test, p, 0)

  for p in range(0,len(test_del),1):
    if test_del[p,0] == ref44[0,0]:
      test_del2 = np.delete(test_del, p, 0)


  if test_del2[0,1] > test_del2[1,1]:
      #zona 1
      ref22 = []
      ref22.append([test_del2[0,0],test_del2[0,1],test_del2[0,2],test_del2[0,3],test_del2[0,4],test_del2[0,5]])
      ref33 = []
      ref33.append([test_del2[1,0],test_del2[1,1],test_del2[1,2],test_del2[1,3],test_del2[1,4],test_del2[1,5]])
  else:
      #zona 2
      ref33 = []
      ref33.append([test_del2[0,0],test_del2[0,1],test_del2[0,2],test_del2[0,3],test_del2[0,4],test_del2[0,5]])
      ref22 = []
      ref22.append([test_del2[1,0],test_del2[1,1],test_del2[1,2],test_del2[1,3],test_del2[1,4],test_del2[1,5]])

  ref22 = np.array(ref22)
  ref33 = np.array(ref33)


  ###

  for j in range(0,len(points),1):
    if points[j,5] == ref11[0,5]:
      points[j,5] = 6
    elif points[j,5] == ref22[0,5]:
      points[j,5] = 7
    elif points[j,5] == ref33[0,5]:
      points[j,5] = 8
    else:
      points[j,5] = 9

  for j in range(0,len(points),1):
    if points[j,5] == 6:
      points[j,5] = 0
    elif points[j,5] == 7:
      points[j,5] = 1
    elif points[j,5] == 8:
      points[j,5] = 2
    else:
      points[j,5] = 3

  if h == 0:
    df11 = pd.DataFrame(points)
  elif h==1:
    df22 =  pd.DataFrame(points)
  elif h==2:
    df33 =  pd.DataFrame(points)
  elif h==3:
    df44 =  pd.DataFrame(points)
  elif h==4:
    df55 =  pd.DataFrame(points)
  elif h==5:
    df66 =  pd.DataFrame(points)

df1 = pd.concat([df11, df22, df33, df44, df55, df66])

df1.columns = ['Coord X','Coord Y','Coord Z','Max Prin','Cluster','Zone']

points_test

kmeansx

kmeans6.cluster_centers_

df1

zones_array = df1['Zone'].to_numpy()

w = df1.values
w[:,0:1]

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
all = ax.scatter(w[:,0],w[:,1],w[:,2], 
            c=zones_array, cmap='rainbow',edgecolor='k', s=40, alpha = 0.5)

legend1 = ax.legend(*all.legend_elements(),
                    loc="center left", title="Zona")
ax.add_artist(legend1)

ax.set_title("ZONAS")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.dist = 10

st.pyplot(fig)

# Verificar por zonas

df11.columns = ['Coord X','Coord Y','Coord Z','Max Prin','Cluster','Zone']
df22.columns = ['Coord X','Coord Y','Coord Z','Max Prin','Cluster','Zone']
df33.columns = ['Coord X','Coord Y','Coord Z','Max Prin','Cluster','Zone']
df44.columns = ['Coord X','Coord Y','Coord Z','Max Prin','Cluster','Zone']
df55.columns = ['Coord X','Coord Y','Coord Z','Max Prin','Cluster','Zone']
df66.columns = ['Coord X','Coord Y','Coord Z','Max Prin','Cluster','Zone']

q = df11
zones_array = q['Zone'].to_numpy()

w = q.values
w[:,0:1]

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
all = ax.scatter(w[:,0],w[:,1],w[:,2], 
            c=zones_array, cmap='rainbow',edgecolor='k', s=40, alpha = 0.5)

legend1 = ax.legend(*all.legend_elements(),
                    loc="center left", title="Zones")
ax.add_artist(legend1)

ax.set_title("todos")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.dist = 10

st.pyplot(fig)

