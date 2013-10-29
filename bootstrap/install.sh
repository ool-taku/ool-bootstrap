#!/bin/bash

SCRIPT_HOME=$(cd $(dirname $0);pwd)

adduser bootstrap --disabled-password --gecos ""
sh -c "echo bootstrap        ALL=\(ALL\)       NOPASSWD: ALL >> /etc/sudoers"

LOG_DIR="/var/log/bootstrap"
if [ ! -e  "${LOG_DIR}" ]; then
  mkdir  "${LOG_DIR}"
fi
chown bootstrap:bootstrap "${LOG_DIR}"

INSTALL_DIR="/usr/lib/bootstrap"
if [ ! -e  "${INSTALL_DIR}" ]; then
  mkdir  "${INSTALL_DIR}"
fi

sh -c "echo -n ${INSTALL_DIR} >> /home/bootstrap/verify_server.conf"

ls $SCRIPT_HOME

cp $SCRIPT_HOME"/etc/init.d/bootstrap" "/etc/init.d/"
chown root:root "/etc/init.d/bootstrap"
cp $SCRIPT_HOME"/usr/bin/bootstrap" "/usr/bin/"
chown root:root "/usr/bin/bootstrap" 
cp -R "${SCRIPT_HOME}/db" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/etc" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/keys" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/lib" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/log" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/scenario" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/scripts" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/settings" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/templates" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/tmp" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/usr" "${INSTALL_DIR}"
cp -R "${SCRIPT_HOME}/web" "${INSTALL_DIR}"

chown -R bootstrap:bootstrap "${INSTALL_DIR}"

service bootstrap start
update-rc.d bootstrap defaults

