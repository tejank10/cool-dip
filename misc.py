def clipimg(img, tau1=0, tau2=255)
    g = np.clip(img, tau1, tau2)
    return g

def miximgs(img1, img2, alpha=0.5):
    mixed_img = alpha*img1 + (1-alpha)*img2
    return mixed_img