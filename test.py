import numpy as np

def double_shuffle(x_train, y_train):
    #shuffle x and y together
    p = np.random.permutation(len(x_train))
    x_train = x_train[p]
    y_train = y_train[p]
    
def get_holdout_err(x, y, x_hold, y_hold, lam):  

    w = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(x), x) + lam * np.identity(x.shape[1])), np.transpose(x)), y)
    print lam
    print w
    predict = np.dot(x_hold, w)
    print predict
    holdout_err = np.mean((np.dot(x_hold, w) - y_hold) ** 2)   
    return holdout_err

def narrow_lambda_range(x_tt, y_tt, x_hd, y_hd, lam_range, prev_min_err):
    print lam_range
    errs = []
    for lam in lam_range:
        holdout_err = get_holdout_err(x_tt, y_tt, x_hd, y_hd, lam)
        errs.append(holdout_err)
    print errs
    min_err = min(errs)
    idx = np.argmin(errs)
    best_lam = lam_range[idx]
    #print "lambad: %f, min err: %.3f" % (best_lam, min_err)
    err_diff = abs(min_err - prev_min_err)
    if err_diff < 0.01:
        return best_lam
    else:
        if idx==0 or idx==len(lam_range)-1:
            return best_lam
        else:
            new_lam_range = np.linspace(lam_range[idx-1], lam_range[idx+1], 100)
            return narrow_lambda_range(x_tt, y_tt, x_hd, y_hd, new_lam_range, min_err)
        

def standalize_col(arr):
    for j in range(arr.shape[1]):
        print j
        cmean = np.mean(arr[:,j])
        print cmean
        cstd = np.std(arr[:,j])
        print cstd
        arr[:,j] = (arr[:,j]-cmean)/float(cstd)
    return arr

if __name__ == '__main__':
    X1 = np.array([[1.0,2.0,], 
                  [4,6,],
                  [7,1,]])
    X2 = np.array([[1], 
                  [11]])
    X3 = np.array([[1, 2], 
                  [3, 4]])
    X4 = np.array([1,2,3,4,5])
    
    print np.dot(X3, X2)
#     #X = np.concatenate((X1, X2), axis=1)
#     p = np.random.permutation(len(X1))
#     print p
#     X1 = X1[p]
#     X2 = X2[p]
#     print X1
#     print X2
#     #print np.random.shuffle(X1, X2, random_state=0)

#     X1 = standalize_col(X1)
#     print X1

#     N = np.array([[0.89166923,0.34872353], 
#               [0.34872353,0.72069768]])
#     
#     N = np.array([[1.00701763,0.43806633], 
#           [0.43806633,1.00701763]])
#     
#     #v = [0.18117706,  1.11553858]
#     v = [0.20461457,  1.55872135]
#     print np.dot(N, v)