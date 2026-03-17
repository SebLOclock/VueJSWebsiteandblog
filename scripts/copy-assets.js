const fs = require('fs')
const path = require('path')

const sourceDir = path.join(__dirname, '../public')
const targetDir = path.join(__dirname, '../dist')

function copyRecursive(src, dest) {
  if (!fs.existsSync(src)) return

  const stats = fs.statSync(src)

  if (stats.isDirectory()) {
    if (!fs.existsSync(dest)) {
      fs.mkdirSync(dest, { recursive: true })
    }
    fs.readdirSync(src).forEach(child => {
      copyRecursive(path.join(src, child), path.join(dest, child))
    })
  } else {
    fs.copyFileSync(src, dest)
  }
}

// Créer le dossier dist s'il n'existe pas
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true })
}

// Copier récursivement le contenu de public vers dist
if (fs.existsSync(sourceDir)) {
  fs.readdirSync(sourceDir).forEach(entry => {
    copyRecursive(
      path.join(sourceDir, entry),
      path.join(targetDir, entry)
    )
  })
  console.log('Assets statiques copiés avec succès !')
} else {
  console.log('Aucun asset statique à copier (dossier public non trouvé)')
}
