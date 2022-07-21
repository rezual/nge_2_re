#!/bin/bash

set -ex

export PYTHONIOENCODING=utf-8

GAME_UNPACKED_ISO_PATH="./unpacked"
GAME_USRDIR_PATH="$GAME_UNPACKED_ISO_PATH/PSP_GAME/USRDIR"

GAME_GLOBAL_TRANSLATION_PHRASES="./translations/global_translation.json"

function patch_bind() {
	BIND_PATH="$1"

	ORIGINAL_BIND_PATH="${GAME_USRDIR_PATH}/${BIND_PATH}"
	ORIGINAL_BIND_UNPACKED_PATH="${ORIGINAL_BIND_PATH}.BINDPACK"
	BACKUP_BIND_PATH="${ORIGINAL_BIND_PATH}.BACKUP"
	BACKUP_BIND_UNPACKED_PATH="${BACKUP_BIND_PATH}.BINDPACK"

	# Check if the backup exists
	if [ ! -f "${BACKUP_BIND_PATH}" ]; then
		# Create it from the existing original
		if [ ! -f "${ORIGINAL_BIND_PATH}" ]; then
			echo 'Could not find the following file:'
			echo "  MISSING: ${ORIGINAL_BIND_PATH}"
			echo 'Did you properly extract the contents of the .iso to'
			echo "the '${GAME_UNPACKED_ISO_PATH}/' directory?"
			exit 1
		fi

		cp "${ORIGINAL_BIND_PATH}" "${BACKUP_BIND_PATH}"
	fi

	# Unpack the backup bind
	if [ ! -d "${BACKUP_BIND_UNPACKED_PATH}" ]; then
		tools/bind.py --unpack "${BACKUP_BIND_PATH}"
	fi

	# Patch the contents of the bind
	for i in "${BACKUP_BIND_UNPACKED_PATH}/"*.bin
	do
		tools/text.py --patch "$i" "$GAME_GLOBAL_TRANSLATION_PHRASES"
	done 

	# Move the .bin.PATCHED files to a new folder
	if [ ! -d "${ORIGINAL_BIND_UNPACKED_PATH}" ]; then
		mkdir "${ORIGINAL_BIND_UNPACKED_PATH}"
	else
		find "${ORIGINAL_BIND_UNPACKED_PATH}" -mindepth 1 -maxdepth 1 -type f -exec rm {} \;
	fi
	mv "${BACKUP_BIND_UNPACKED_PATH}/"*.bin.PATCHED "${ORIGINAL_BIND_UNPACKED_PATH}/"
	
	# Rename .bin.PATCHED to just .bin
	find "${ORIGINAL_BIND_UNPACKED_PATH}/" -name "*.bin.PATCHED" -exec sh -c 'mv $0 `dirname "$0"`/`basename "$0" .bin.PATCHED`.bin' '{}' \; 
	
	# Rebind
	tools/bind.py --pack "${ORIGINAL_BIND_UNPACKED_PATH}/"
}

function patch_text() {
	TEXT_PATH="$1"

	ORIGINAL_TEXT_PATH="${GAME_USRDIR_PATH}/${TEXT_PATH}"
	BACKUP_TEXT_PATH="${ORIGINAL_TEXT_PATH}.BACKUP"
	BACKUP_TEXT_PATCHED_PATH="${BACKUP_TEXT_PATH}.PATCHED"

	# Check if the backup exists
	if [ ! -f "${BACKUP_TEXT_PATH}" ]; then
		# Create it from the existing original
		if [ ! -f "${ORIGINAL_TEXT_PATH}" ]; then
			echo 'Could not find the following file:'
			echo "  MISSING: ${ORIGINAL_TEXT_PATH}"
			echo 'Did you properly extract the contents of the .iso to'
			echo "the '${GAME_UNPACKED_ISO_PATH}/' directory?"
			exit 1
		fi

		cp "${ORIGINAL_TEXT_PATH}" "${BACKUP_TEXT_PATH}"
	fi

	tools/text.py --patch "${BACKUP_TEXT_PATH}" "${GAME_GLOBAL_TRANSLATION_PHRASES}"
	mv "${BACKUP_TEXT_PATH}.PATCHED" "${ORIGINAL_TEXT_PATH}"
}

# Patch the BIND files
patch_bind "game/imtext.bin"
patch_bind "btl/btimtext.bin"

# Patch independent TEXT files
patch_text "free/f2info.bin"
patch_text "free/f2tuto.bin"

# Patch the EVS files
# Extract all the *.har files
find "${GAME_USRDIR_PATH}/event" -mindepth 1 -maxdepth 1 -type f -name '*.har' -exec tools/hgar.py --extract "{}" \;

# Patch the evs files
find "${GAME_USRDIR_PATH}/event" -mindepth 2 -maxdepth 2 -type f -name '*.evs' -exec tools/evs.py --patch "{}" "$GAME_GLOBAL_TRANSLATION_PHRASES" \;

# Patch the pictures in the har files
# TODO

# Repack the evs files
find "${GAME_USRDIR_PATH}/event" -mindepth 2 -maxdepth 2 -type f -name '*.evs.PATCHED' -exec sh -c 'tools/hgar.py --replace-raw "`dirname "$0" | sed s/.HGARPACK//g`" "`basename "$0" .PATCHED`" "{}"' '{}' \;

# Move the .har_REPLACE to just be .har
find "${GAME_USRDIR_PATH}/event" -mindepth 1 -maxdepth 1 -type f -name '*.har_REPLACE' -exec sh -c 'mv $0 ${0%_REPLACE}' "{}" \;

# Generate the patch (currently as CWCheat codes for the PPSSPP emulator)
./generate_hook_cwcheat_codes.py > ULJS00064.ini
