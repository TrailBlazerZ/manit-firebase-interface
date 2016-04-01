I am using `Python 2.7.9` with `OpenSSL 1.0.1f 6 Jan 2014` .

On building the following code 

     from firebase import firebase
     firebase = firebase.FirebaseApplication('https://test.firebaseio.com',None)
     data = {'testVal': '0'}
     result = firebase.post('/user', data)
     print (result)


However I got the following error

        File "/usr/local/lib/python2.7/dist-packages/firebase/decorators.py", line 19, in wrapped
          return f(*args, **kwargs)
        File "/usr/local/lib/python2.7/dist-packages/firebase/firebase.py", line 329, in post
          connection=connection)
        File "/usr/local/lib/python2.7/dist-packages/firebase/decorators.py", line 19, in wrapped
          return f(*args, **kwargs)
        File "/usr/local/lib/python2.7/dist-packages/firebase/firebase.py", line 97, in make_post_request
          timeout=timeout)
        File "/usr/local/lib/python2.7/dist-packages/requests/sessions.py", line 340, in post
          return self.request('POST', url, data=data, **kwargs)
        File "/usr/local/lib/python2.7/dist-packages/requests/sessions.py", line 279, in request
          resp = self.send(prep, stream=stream, timeout=timeout, verify=verify, cert=cert, proxies=proxies)
        File "/usr/local/lib/python2.7/dist-packages/requests/sessions.py", line 374, in send
          r = adapter.send(request, **kwargs)
        File "/usr/local/lib/python2.7/dist-packages/requests/adapters.py", line 213, in send
          raise SSLError(e)
      requests.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)

