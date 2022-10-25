source ${PATCHES_DIR}/python3_package.sh
python3_package_setup
python3_package_pip_install "pyyaml"

mkdir -p ${OUTPUT_DIR}${INSTALL_PREFIX}/lib/python3.8/site-packages/amaranth
for target in *; do    
    if [ $target != 'python3' ]; then
        cp -r $target ${OUTPUT_DIR}${INSTALL_PREFIX}/lib/python3.8/site-packages/amaranth/.
    fi
done

cd ${OUTPUT_DIR}${INSTALL_PREFIX}/lib/python3.8/site-packages/amaranth
for target in *; do
    pushd $target
    python3_package_develop "--egg-path ./amaranth/$target"
    popd
done
( find . -type d -name ".git" && find . -name ".gitignore" && find . -name ".gitmodules" && find . -name ".gitattributes" && find . -name ".github" ) | xargs rm -rf

python3_package_pth amaranth

