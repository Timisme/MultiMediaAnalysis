import numpy as np 
import cv2 
from sklearn.mixture import GaussianMixture as GMM 
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix

def GMM_fit(file_name= 'soccer1', second_file= None,  n= 2):

	img= cv2.imread(f'data/{file_name}.jpg')
	# print(img.shape)
	img2 = img.reshape((-1, 3))
	# print(img2.shape)

	if second_file: 
		img = cv2.imread(f'data/{second_file}.jpg')
		img3 = img.reshape((-1, 3))
		img2 = np.concatenate((img2, img3), axis= 0)
		# print(f'concat shape: {img2.shape}')

	gmm_model = GMM(n_components= n, covariance_type= 'full', random_state= 39)
	model_fit = gmm_model.fit(img2)

	return model_fit

def GMM_predict(model_fit, file_name):

	img= cv2.imread(f'data/{file_name}.jpg')
	img2 = img.reshape((-1, 3))

	gmm_labels = model_fit.predict(img2)

	# print(gmm_labels)

	original_shape = img.shape 
	results = gmm_labels.reshape(original_shape[0], original_shape[1])
	# print(list(map(lambda x: 0, filter(lambda x: x!=1, results.flatten()))))

	if (n==6) & (q=='Q1') & (file_name=='soccer1'):
		pred= list(map(lambda x: 0 if x!=1 else 1, results.flatten()))
	
	elif (n==6) & (q=='Q2') & (file_name=='soccer2'):
		pred= list(map(lambda x: 0 if x!=2 else 1, results.flatten()))

	elif (n==6) & (q=='Q3') & (file_name=='soccer1'):
		pred= list(map(lambda x: 0 if x!=1 else 1, results.flatten()))

	elif (n==6) & (q=='Q3') & (file_name=='soccer2'):
		pred= list(map(lambda x: 0 if x!=2 else 1, results.flatten()))

	elif (n==5) & (q=='Q1') & (file_name=='soccer1'):
		pred= list(map(lambda x: 0 if x!=1 else 1, results.flatten()))
	
	elif (n==5) & (q=='Q2') & (file_name=='soccer2'):
		pred= list(map(lambda x: 0 if x!=2 else 1, results.flatten()))

	elif (n==5) & (q=='Q3') & (file_name=='soccer1'):
		pred= list(map(lambda x: 0 if x!=2 else 1, results.flatten()))

	elif (n==5) & (q=='Q3') & (file_name=='soccer2'):
		pred= list(map(lambda x: 0 if x!=1 else 1, results.flatten()))

	elif (n==4) & (q=='Q2') & (file_name=='soccer2'):
		pred= list(map(lambda x: 0 if x!=0 else 1, results.flatten()))

	elif (n==4) & (q!='Q2'):
		pred= list(map(lambda x: 0 if x!=1 else 1, results.flatten()))

	elif (n==3) & (q=='Q2') & (file_name=='soccer2'):
		pred= list(map(lambda x: 0 if x!=2 else 1, results.flatten()))

	elif (n==3) & (q!='Q2'):
		pred= list(map(lambda x: 0 if x!=1 else 1, results.flatten()))

	elif (n==2) & (q=='Q2') & (file_name=='soccer2'):
		pred= list(map(lambda x: 0 if x!=0 else 1, results.flatten()))

	elif (n==2) & (q!='Q2'):
		pred= list(map(lambda x: 0 if x!=1 else 1, results.flatten()))

	results = np.array(pred).reshape(original_shape[0], original_shape[1])

	gt_img = cv2.imread(f'data/{file_name}_mask.png')
	# print(gt_img)
	gray_gt_img = cv2.cvtColor(gt_img, cv2.COLOR_BGR2GRAY)
	gt = (gray_gt_img/255).flatten()

	# cv2.imshow(f'{file_name}_pred', results.astype('uint8')*255)
	# while cv2.waitKey(100) != 27:# loop if not get ESC
	#     if cv2.getWindowProperty(f'{file_name}_pred',cv2.WND_PROP_VISIBLE) <= 0:
	#         break

	status = cv2.imwrite(f'{file_name}_pred_{n}_{q}.jpg', results.astype('uint8')*255)
	# print('-'*50)
	# print(f'report:\n{classification_report(pred, gt)}')

	return accuracy_score(pred, gt).round(2), f1_score(pred, gt).round(2), precision_score(pred,gt).round(2), recall_score(pred, gt).round(2)

if __name__ == '__main__':
	# ns = [2, 3, 4, 5, 6]
	Qs = ['Q1', 'Q2', 'Q3']
	ns= [4]
	global n 
	global q 

	for n in ns:
		for q in Qs:

			print(f'n: {n}')

			if q == 'Q1':
				print('Q1...')
				model_fit = GMM_fit(file_name= 'soccer1', n= n)
				a, f1, p, r = GMM_predict(model_fit= model_fit, file_name= 'soccer1')
				print(f'pic: soccer1\naccuracy: {a}\nf1_score: {f1}\n')
			elif q == 'Q2':

				print('Q2...')
				a, f1, p, r = GMM_predict(model_fit= model_fit, file_name= 'soccer2')
				print(f'pic: soccer2\naccuracy: {a}\nf1_score: {f1}\n')
			elif q == 'Q3':
				print('Q3...')
				model_fit = GMM_fit(file_name= 'soccer1', second_file= 'soccer2', n= n)
				a, f1, p, r = GMM_predict(model_fit= model_fit, file_name= 'soccer1')
				print(f'pic: soccer1\naccuracy: {a}\nf1_score: {f1}\n')
				a, f1, p, r = GMM_predict(model_fit= model_fit, file_name= 'soccer2')
				print(f'pic: soccer2\naccuracy: {a}\nf1_score: {f1}')

		print('-'*50)


