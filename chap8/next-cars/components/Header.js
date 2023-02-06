import Link from "next/Link"
import useAuth from "../hooks/useAuth";
import { useEffect } from "react";

export default function Header() {
	
	const { user, setUser, authError, setAuthError, setLoading, loading } = useAuth();
	  useEffect(() => {
	    setLoading(true);
	    (async () => {
	      const userData = await fetch("/api/user");
	      try {
	        const user = await userData.json();
	        setUser(user);
	      } catch (error) {
	        setUser(null);
	      }
	    })();
	    setLoading(false);
	  }, []);
	
	return(
		<>
		<div className="text-orange-600 p-2 font-bold flex flex-row justify-between items-center">
		<div>
		{loading ? <span>Loading...</span> : ""}
		<Link href="/">
		 FARM Cars
		 
		 {user ? (
		               <span>
		                 {user.username} ({user.role})
		               </span>
		             ) : (
		               ""
		             )}
		</Link>
		</div>
		<ul className="flex flex-row space-x-4">
		<li>
		<Link href="/cars">
		Cars
		</Link>
		</li>
		{user && user.role === "ADMIN" ? (
		          <li>
		            <Link href="/cars/add">
		              <a>Add Car</a>
		            </Link>
		          </li>
		        ) : (
		          ""
		        )}
		        {!user ? (
			
			<>
		
		<li>
		<Link href="/account/register">
		Register
		</Link>
		</li>
		<li>
		<Link href="/account/login">
		Login
		</Link>
		</li>
		
		 </>
		        ) : (
		          <>
		            <li>
		              <Link href="/account/logout">
		                <a>Log out {user.username}</a>
		              </Link>
		            </li>
		          </>
		        )}
		</ul>

		</div>
		</>
	)
} 