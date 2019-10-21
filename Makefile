
benchmark:
	cd benchmarks && $(MAKE) $@

build-dependencies:
	src/install-dependencies.sh

clean:
	rm benchmarks/img/*-crunch.png

dist: 
	./dmg-builder.sh

dist-homebrew:
	cask-repair crunch

install-executable:
	sudo cp src/crunch.py /usr/local/bin/crunch
	@echo " "
	@echo "[*] crunch executable installed on path /usr/local/bin/crunch"
	@echo "[*] Usage: $ crunch [image path 1]...[image path n]"

install-macos-service:
	- sudo rm -rf ~/Library/Services/Crunch\ Image\(s\).workflow
	sudo cp -R service/Crunch\ Image\(s\).workflow ~/Library/Services/Crunch\ Image\(s\).workflow
	@echo " "
	@echo "[*] Crunch Image(s) macOS service installed on the path ~/Library/Services/Crunch\ Image\(s\).workflow"
	@echo " "
	@echo "[*] You can use the Crunch service by right clicking on one or more PNG files, then select Services > Crunch Image(s)"

uninstall-dependencies:
	sudo rm -rf ~/pngquant
	sudo rm -rf ~/zopfli
	@echo " "
	@echo "[*] Dependency removal complete."

uninstall-executable:
	sudo rm /usr/local/bin/crunch
	@echo " "
	@echo "[*] crunch executable uninstall complete."

uninstall-macos-service:
	sudo rm -rf ~/Library/Services/Crunch\ Image\(s\).workflow
	@echo " "
	@echo "[*] The Crunch Image(s) macOS service was removed from your system"

test-coverage:
	./coverage.sh

test-python:
	tox
	flake8 --ignore=E501,W503,E121,E123,E126,E226,E24,E704,W503,W504,N806 src/crunch.py

test-shell:
	shellcheck --exclude=2046 src/*.sh

test-valid-png-output:
	crunch testfiles/*.png
	pngcheck testfiles/*-crunch.png
	rm testfiles/*-crunch.png

test: test-python test-shell test-valid-png-output


.PHONY: benchmark build-dependencies install-executable install-macos-service uninstall-executable uninstall-macos-service test test-coverage test-python test-shell test-valid-png-output dist