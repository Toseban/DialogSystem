require 'rake/testtask'

task default: :build

desc 'Builds the App.'
task build: 'DialogSystem/DialogSystem.jar'

task :format do
  options = []
  options.push '--replace' if ENV['repair']
  sh "gherkin_format #{options.join ' '} features/*.feature"
end

task run: 'DialogSystem/DialogSystem.jar' do
  sh "#{ENV['JAVAHOME']}/bin/java -cp DialogSystem/resources:DialogSystem/DialogSystem.jar:#{FileList['DialogSystem/lib/*.jar'].join ':'} de.roboy.dialog.DialogSystem" 
end

file 'DialogSystem/DialogSystem.jar' do
  cd('DialogSystem') do 
    mkdir_p 'package'
    sh 'cp -r resources package'
    sh "#{ENV['JAVAHOME']}/bin/javac #{FileList['src/**/*.java']} -cp #{FileList['lib/*.jar'].join ':'} -d package"
    sh "#{ENV['JAVAHOME']}/bin/jar cfm DialogSystem.jar Manifest.txt -C package/ ."
  end
end