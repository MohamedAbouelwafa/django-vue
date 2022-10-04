echo "============================== Building Vue Js static files =============================="
pushd vueapp > null
yarn build

echo "============================== Collecting Django static files =============================="
popd > null
./manage.py collectstatic --noinput

echo "============================== Django/VueJs artifacts are ready for deployment =============================="
