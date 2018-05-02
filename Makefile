
build-dependencies:
	src/install-dependencies.sh

install-executable:
	sudo cp src/crunch /usr/local/bin/crunch
	@echo " "
	@echo "[*] crunch executable installed on path /usr/local/bin/crunch"
	@echo "[*] Usage: $ crunch [image path 1]...[image path n]"

install-macos-service:
	sudo cp -R service/Crunch\ Image\(s\).workflow ~/Library/Services/Crunch\ Image\(s\).workflow
	@echo " "
	@echo "[*] Crunch Image(s) macOS service installed on the path ~/Library/Services/Crunch\ Image\(s\).workflow"
	@echo " "
	@echo "[*] You can use the Crunch service by right clicking on one or more PNG files, then select Services > Crunch Image(s)"

uninstall-dependencies:
	sudo rm -rf ~/pngquant
	sudo rm -rf ~/zopfli
	@echo " "
	@echo "[*] Dependencies removed."

uninstall-executable:
	sudo rm /usr/local/bin/crunch
	@echo " "
	@echo "[*] crunch executable uninstall complete"

uninstall-macos-service:
	sudo rm -rf ~/Library/Services/Crunch\ Image\(s\).workflow
	@echo " "
	@echo "[*] The Crunch Image(s) macOS service was removed from your system"

test-python:
	flake8 --ignore=E501,W503 src/*.py

test-shell:
	shellcheck --exclude=2046 src/*.sh

test: test-python test-shell

.PHONY: build-dependencies install-executable install-macos-service uninstall-executable uninstall-macos-service test test-python test-shell