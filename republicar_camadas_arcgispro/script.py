import arcpy
import os, sys
from arcgis.gis import GIS
from dotenv import load_dotenv
# Estamos utilizando aqui um Script que utiliza o login do ArcGIS Pro, logo você precisa estar logado com o mesmo usuário que publicou as informações para que dê certo

# Variáveis de ambiente
load_dotenv()
PROJECT = os.getenv("PROJECT")
SERVICE_NAME = os.getenv("SERVICE_NAME")

# Obtendo caminho. Coloque o Script na mesma pasta do projeto do ArcGIS Pro
pasta = os.getcwd()
prjPath = pasta + PROJECT

# Variáveis a serem atualizadas:
# Nome da Feature service/SD no arcgis.com
sd_fs_name = SERVICE_NAME
sd_sddraft = sd_fs_name + ".sddraft"
sd_sd = sd_fs_name + ".sd"
# Opções de Compartilhamento
shrOrg = True
shrEveryone = True
shrGroups = ""

### Final do estabelecimento das variáveis

# Pasta local onde vão ficar os arquivos temporários
relPath = os.path.dirname(prjPath)
sddraft = os.path.join(relPath, sd_sddraft)
sd = os.path.join(relPath, sd_sd)

# Criando um novo serviço e realizando o overwrite da feição
print("Creating SD file")
arcpy.env.overwriteOutput = True
prj = arcpy.mp.ArcGISProject(prjPath)
mp = prj.listMaps()[0]
arcpy.mp.CreateWebLayerSDDraft(mp, sddraft, sd_fs_name, 'MY_HOSTED_SERVICES', 'FEATURE_ACCESS','', True, True, allow_exporting=True)
arcpy.StageService_server(sddraft, sd)

print("\n\nActive Portal in ArcGIS Pro")
gis = GIS("pro")

# Procurando o SD, realizando o update, Publicando /w Sobrescrevendo e compartilhando os dados
sdItem = gis.content.search("{}".format(sd_fs_name), item_type="Service Definition")[0]
print("Found SD: {}, ID: {} n Uploading and overwriting…".format(sdItem.title, sdItem.id))
sdItem.update(data=sd)
print("Overwriting existing feature service…")
fs = sdItem.publish(overwrite=True)

if shrOrg or shrEveryone or shrGroups:
  print("Setting sharing options…")
  fs.share(org=shrOrg, everyone=shrEveryone, groups=shrGroups)

print("Finished updating: {} – ID: {}".format(fs.title, fs.id))