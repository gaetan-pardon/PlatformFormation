
# kmeans
import random
import matplotlib.pyplot as plt

nombre_centroid=7
nombre_iteration=1000
data_n_samples=500
data_n_features=2
data_centers=5
data_cluster_std=1.50
precision=1e-8

def generate_data(n_samples=300, n_features=2, centers=3, cluster_std=1.0):
    data = []
    for i in range(centers):
        center = [random.uniform(-10, 10) for _ in range(n_features)]
        for _ in range(n_samples ):
            point = [coord + random.gauss(0, cluster_std) for coord in center]
            data.append(point)
    return data


def kmeans(data, nombre_centroid, nombre_iteration= 10000000 , precision=1e-4):
    # Initialisation des centroids
    #centroids = data.sample(n=nombre_centroid).values
    if nombre_centroid > len(data):
        raise ValueError("nombre_centroid est superieur aux nombre de points dans les données")
    centroids = random.sample(data, k=nombre_centroid)
    plt.scatter([point[0] for point in data], [point[1] for point in data], c='black')
    plt.scatter([centroid[0] for centroid in centroids], [centroid[1] for centroid in centroids], c='red', marker='X')
    plt.title(f'Condition initiale')
    plt.show()
    modification = precision + 1

    i=0
    while i < nombre_iteration and modification > precision:
        # Assignation des points aux centroids les plus proches
        closest_centroids = []
        for point in data:
            distances = []
            for selected_centre in range(nombre_centroid):
                distance = 0
                for selected_dimention in range(len(point)):
                    distance += (point[selected_dimention] - centroids[selected_centre][selected_dimention]) ** 2
                distances.append(distance)
            #distances = [sum((point[j] - centroids[k][j]) ** 2 for j in range(len(point))) for k in range(nombre_centroid)]
            #closest_centroids.append(distances.index(min(distances)))
            min_distance = float('inf')
            closest_centroid = 0
            for k in range(nombre_centroid):
                if distances[k] < min_distance:
                    min_distance = distances[k]
                    closest_centroid = k
            closest_centroids.append(closest_centroid)

        # Mise à jour des centroids
        #new_centroids = []
        somme_points_par_centroid = []
        for k in range(nombre_centroid):
            somme_points_par_centroid.append([[],0])
            for index_point in range(len(data)):
                point = data[index_point]
                if closest_centroids[index_point] == k:
                    if somme_points_par_centroid[k][1] > 0:
                        for selected_dimention in range(len(point)):
                            somme_points_par_centroid[k][0][selected_dimention] += point[selected_dimention]         
                    else:
                        for selected_dimention in range(len(point)):
                            somme_points_par_centroid[k][0].append(point[selected_dimention])
                    somme_points_par_centroid[k][1] += 1

        modification = 0
        for k in range(nombre_centroid):
            if somme_points_par_centroid[k][1] > 0 :
                #new_coordonates = []
                for selected_dimention in range(len(somme_points_par_centroid[k][0])):
                    modification += (somme_points_par_centroid[k][0][selected_dimention] / somme_points_par_centroid[k][1] - centroids[k][selected_dimention]) ** 2
                    centroids[k][selected_dimention] = somme_points_par_centroid[k][0][selected_dimention] / somme_points_par_centroid[k][1]

        
          
        i+=1
        #mathplotlip affichage a chaque iteration
        plt.clf()
        plt.scatter([point[0] for point in data], [point[1] for point in data], c=closest_centroids, cmap='viridis')
        plt.scatter([centroid[0] for centroid in centroids], [centroid[1] for centroid in centroids], c='red', marker='X')
        plt.title(f'Iteration {i}')
        plt.show(block=False)
        plt.pause(0.2)
    
    plt.show()

    return centroids, closest_centroids


def main():
    print("K-means clustering")
    data = generate_data(n_samples=data_n_samples, n_features=data_n_features, centers=data_centers, cluster_std=data_cluster_std)
    print("Data generated")
    centroids, closest_centroids = kmeans(data=data, nombre_centroid=nombre_centroid, nombre_iteration=nombre_iteration, precision=precision)
    print("Centroids:", centroids)
    #print("Closest Centroids:", closest_centroids)


if __name__ == "__main__":
    main()