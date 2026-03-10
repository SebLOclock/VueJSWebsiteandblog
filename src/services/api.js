const API_BASE_URL = 'https://blog.sebastienlemoine.fr/wp-json/wp/v2'
const PVC_API_URL = 'https://blog.sebastienlemoine.fr/wp-json/post-views-counter'

const fetchOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  mode: 'cors',
  credentials: 'omit'
}

export const fetchPosts = async (perPage = 10) => {
  try {
    const response = await fetch(`${API_BASE_URL}/posts?_embed&per_page=${perPage}`, fetchOptions)
    
    if (!response.ok) {
      throw new Error(`Erreur HTTP: ${response.status}`)
    }
    return await response.json()
  } catch (error) {
    console.error('Erreur lors de la récupération des articles :', error)
    throw error
  }
}

export const fetchPostBySlug = async (slug) => {
  try {
    const url = `${API_BASE_URL}/posts?slug=${encodeURIComponent(slug)}&_embed`
    
    const response = await fetch(url, fetchOptions)
    
    if (!response.ok) {
      throw new Error(`Erreur HTTP: ${response.status}`)
    }
    
    const data = await response.json()
    
    if (!data || data.length === 0) {
      throw new Error(`Aucun article trouvé avec le slug: ${slug}`)
    }
    
    return data[0]
  } catch (error) {
    console.error('Erreur lors de la récupération de l\'article :', error)
    throw error
  }
}

export const incrementPostViews = async (postId) => {
  try {
    const url = `${PVC_API_URL}/view-post/${postId}`
    
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    
    if (!response.ok) {
      throw new Error(`Erreur HTTP: ${response.status}`)
    }
    
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Erreur lors de l\'incrémentation des vues :', error)
    throw error
  }
} 