#################################
# KNN
#################################

from sklearn.neighbors import KNeighborsClassifier

# 1.dataset 생성
grape = [8, 5]   
fish = [2, 3]
carrot = [7, 10] 
orange = [7, 3]
celery = [3, 8] 
cheese = [1, 1] 

know = [grape,fish,carrot,orange,celery,cheese]  # 중첩 list
y_class = [0, 1, 2, 0, 2, 1] 
class_label = ['과일', '단백질', '채소'] 
 
# 2. 분류기 
knn = KNeighborsClassifier(n_neighbors = 3) # k=3 
model = knn.fit(X = know, y = y_class) 
know 

x1 = 4
X2 = 8

unKnow = [[x1, X2]]

y_pred = model.predict(X = unKnow)
print(y_pred)

print('분류결과 : ',class_label[y_pred[0]]) 
print('분류결과 : ',class_label[y_pred[0]]) 
print('분류결과 : ',class_label[y_pred[0]])

