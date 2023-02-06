import '@/styles/globals.css'
import Header from '../components/Header'
import Footer from '../components/Footer'
import {AuthProvider} from '../context/AuthContext'

export default function App({ Component, pageProps }) {
  return (
    <AuthProvider>
    <div className="min-h-screen flex flex-col justify-between items-stretch">
    <Header />
    <div className="flex-1">
    <Component {...pageProps} />
    </div>
    <Footer/>
    </div>
    </AuthProvider>
    
    
  )
 
}
