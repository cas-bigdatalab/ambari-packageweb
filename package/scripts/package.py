import os
from time import sleep
from resource_management import *

class PackageWebMaster(Script):

    
    def install(self, env):       
        import params
        self.install_packages(env)
        Directory(params.packageweb_dir,
              mode=0755
          )
        Execute('cd ' + params.packageweb_dir + '; wget ' + params.download_url + ' -O packageweb.jar ')               
               

    def configure(self, env):                         
        print("config")

    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        Execute(format('cd {packageweb_dir}; nohup {java64_home}/bin/java -jar packageweb.jar > {log_file} 2>&1& echo $! > /var/run/packageweb.pid'))

    def stop(self, env):
        Execute('kill -9 `cat /var/run/packageweb.pid`')

    def restart(self, env):
        print("restart")
        self.stop(env)
        self.start(env)

    def status(self, env):
        check_process_status('/var/run/packageweb.pid')


if __name__ == "__main__":
    PackageWebMaster().execute()
