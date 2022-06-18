
benchmark:
	cd benchmarks && $(MAKE) $@

build-dependencies:
	src/install-dependencies.sh

build-macos-icns:
	rm -rf img/CrunchIcon.iconset
	mkdir img/CrunchIcon.iconset
	sips -z 16 16     img/Crunch-icon-3.png --out img/CrunchIcon.iconset/icon_16x16.png
	sips -z 32 32     img/Crunch-icon-3.png --out img/CrunchIcon.iconset/icon_16x16@2x.png
	sips -z 32 32     img/Crunch-icon-3.png --out img/CrunchIcon.iconset/icon_32x32.png
	sips -z 64 64     img/Crunch-icon-3.png --out img/CrunchIcon.iconset/icon_32x32@2x.png
	sips -z 128 128   img/Crunch-icon-3.png --out img/CrunchIcon.iconset/icon_128x128.png
	sips -z 256 256   img/Crunch-icon-3.png --out img/CrunchIcon.iconset/icon_128x128@2x.png
	sips -z 256 256   img/Crunch-icon-3.png --out img/CrunchIcon.iconset/icon_256x256.png
	sips -z 512 512   img/Crunch-icon-3.png --out img/CrunchIcon.iconset/icon_256x256@2x.png
	cd img && iconutil -c icns CrunchIcon.iconset

build-macos-installer:
	# https://github.com/sindresorhus/create-dmg
	-rm bin/*.dmg
	-cd bin && create-dmg Crunch.app
	# create checksum file for the installer
	cd bin && mv Crunch*.dmg Crunch-Installer.dmg
	cd bin && shasum -a 256 Crunch-Installer.dmg > Crunch-Installer-checksum.txt

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
	flake8 src/crunch.py

test-shell:
	shellcheck --exclude=2046 src/*.sh

test-valid-png-output:
	src/crunch.py testfiles/*.png
	pngcheck testfiles/*-crunch.png
	rm testfiles/*-crunch.png

test: test-python test-shell test-valid-png-output


.PHONY: benchmark build-dependencies install-executable install-macos-service uninstall-executable uninstall-macos-service test test-coverage test-python test-shell test-valid-png-output dist