import cookie from 'cookie'

export default async (req, res) => {
	res.status(200),setHeader('Set-Cookie', cookie.seralizer (
		'jwt', '',
		{
			path: '/',
			httpOnly: true,
			sameSite: 'strict',
			maxAge: -1
		}
	)).end()
}