##thexnews.com
The blog thexnews.com souce code originally forked from EnigmaCurry blogofile `blog_features` example.

##Readme in russian
http://thexnews.com/статический-блог-blogofile.html

##Install
    #install dependencies
    sudo apt-get install python-setuptools python-django python-twisted-web
    sudo apt-get install node-uglify python-utidylib

    #install cssoptimizer
    wget --content-disposition http://mabblog.com/getfile.php?file=37
    sudo tar -xvf cssoptimizer_linux.tgz -C /usr/bin ./cssoptimizer

    #install blogofile
    sudo easy_install Blogofile==0.7.1

    #clone thexnews.com
    git clone git://github.com/dima2/thexnews.com.git

    #build blog and run blogofile server
    cd thexnews.com/
    ./deploy_localhost.sh