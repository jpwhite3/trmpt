CDW="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd) "

init: build
	@echo ""

clean:
	@echo "Cleaning"
	-cd dist; rm -rf *
	-cd src; rm -rf __pycache__
	-cd deps; rm -rf __pycache__
	@echo "Making directories"
	-mkdir deps
	-mkdir dist

prep: clean
	@echo "Getting dependancies"
	cd deps; pip install -r ../requirements.txt --target=./
	cd deps; zip -r9q ../src/vendor.zip ./*

build: prep
	@echo "Building"
	cd src; zip -r9q ../dist/trmpt-app.zip ./*

install:
	@echo "Deploying"
	aws lambda update-function-code --function-name FakeDataGeneratorFunction --zip-file fileb://./dist/trmpt-app.zip
