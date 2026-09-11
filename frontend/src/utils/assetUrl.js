export const assetUrl = (assetPath) => {
  if (!assetPath) return assetPath
  if (/^(https?:)?\/\//.test(assetPath) || assetPath.startsWith('data:')) {
    return assetPath
  }

  const baseUrl = import.meta.env.BASE_URL
  const normalizedPath = assetPath.replace(/^\/+/, '')
  return `${baseUrl}${normalizedPath}`
}