'''  
  K Thyng copying from P. Kovesi and translating from Matlab to Python
  2020/5/22
  
  NORMALISE - Normalises image values to 0-1, or to desired mean and variance
 
  Usage:
             n = normalise(im)
 
  Offsets and rescales image so that the minimum value is 0
  and the maximum value is 1.  Result is returned in n.  If the image is
  colour the image is converted to HSV and the value/intensity component
  is normalised to 0-1 before being converted back to RGB.
 
 
              n = normalise(im, reqmean, reqvar)
 
  Arguments:  im      - A grey-level input image.
              reqmean - The required mean value of the image.
              reqvar  - The required variance of the image.
 
  Offsets and rescales image so that it has mean reqmean and variance
  reqvar.  Colour images cannot be normalised in this manner.

  Copyright (c) 1996-2005 Peter Kovesi
  School of Computer Science & Software Engineering
  The University of Western Australia
  http://www.csse.uwa.edu.au/
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, subject to the following conditions:
  
  The above copyright notice and this permission notice shall be included in 
  all copies or substantial portions of the Software.
 
  The Software is provided "as is", without warranty of any kind.

  January 2005 - modified to allow desired mean and variance
'''
from skimage.color import rgb2hsv, hsv2rgb
import numpy as np

def normalize(im, reqmean=None, reqvar=None):
    
    # Normalize 0–1
    if reqmean is None and reqvar is None:
        
        if im.ndim == 3:
            hsv = rgb2hsv(im)
            v = hsv[:,:,2]
            v = v - np.min(v)     # Just normalise value component
            v = v/np.max(v)
            hsv[:,:,2] = v
            n = hsv2rgb(hsv)
        else:
#             if ~isa(im,'double'), im = double(im); end
            n = im - np.min(im)
            n = n/np.max(n)

    else:  # Normalise to desired mean and variance

        if im.ndim == 3:         # colour image?
            error('cannot normalise colour image to desired mean and variance');

#         if ~isa(im,'double'), im = double(im); end	
        im = im - np.mean(im)    
        im = im/np.std(im)      # Zero mean, unit std dev

        n = reqmean + im*np.sqrt(reqvar)
            
    return n