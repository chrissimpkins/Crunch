all: install-service

install-service:
	sudo cp -R service/Crunch\ Image\(s\).workflow ~/Library/Services/Crunch\ Image\(s\).workflow
	@echo " "
	@echo "[*] Crunch Image(s) macOS service installed on the path ~/Library/Services/Crunch\ Image\(s\).workflow"
	@echo " "
	@echo "[*] You can use the Crunch service by right clicking on one or more PNG files, then select Services > Crunch Image(s)"
	
uninstall-service:
	sudo rm -rf ~/Library/Services/Crunch\ Image\(s\).workflow
	@echo " "
	@echo "[*] The Crunch Image(s) macOS service was removed from your system"

.PHONY: all install-service uninstall-service