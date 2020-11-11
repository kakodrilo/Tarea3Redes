"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo


class Red1( Topo ):
	# Topologia de la Red 1
	
	def __init__( self ):
		# Definir la topologia
		
		# iniciar la topologia
		Topo.__init__( self )

		# Se aniaden los 6 hosts
		HostA = self.addHost( 'hA' , mac = '00:00:00:00:00:01')
		HostB = self.addHost( 'hB' , mac = '00:00:00:00:00:02')
		HostC = self.addHost( 'hC' , mac = '00:00:00:00:00:03')
		HostD = self.addHost( 'hD' , mac = '00:00:00:00:00:04')
		HostE = self.addHost( 'hE' , mac = '00:00:00:00:00:05')
		HostF = self.addHost( 'hF' , mac = '00:00:00:00:00:06')
		
		# Se aniaden los 3 switchs
		SwitchX = self.addSwitch( 's1', dpid="1" )
		SwitchY = self.addSwitch( 's2', dpid="2" )
		SwitchZ = self.addSwitch( 's3', dpid="3" )
		
		# conexiones entre host y switch
		self.addLink( HostA, SwitchX, 0, 1 )
		self.addLink( HostB, SwitchX, 0, 2 )
		
		self.addLink( HostC, SwitchY, 0, 3 )
		self.addLink( HostD, SwitchY, 0, 4 )
		
		self.addLink( HostE, SwitchZ, 0, 5 )
		self.addLink( HostF, SwitchZ, 0, 6 )
		
		# conexiones entre switches
		self.addLink( SwitchX, SwitchY, 7, 8 )
		self.addLink( SwitchX, SwitchZ, 9, 10 )
		self.addLink( SwitchY, SwitchZ, 11, 12 )


class Red2( Topo ):
	# Topologia de la Red 2
	
	def __init__( self ):
		# Definir la topologia
		
		# iniciar la topologia
		Topo.__init__( self )

		# Se aniaden los 6 hosts
		HostA = self.addHost( 'hA' , mac = '00:00:00:00:00:01' )
		HostB = self.addHost( 'hB' , mac = '00:00:00:00:00:02' )
		HostC = self.addHost( 'hC' , mac = '00:00:00:00:00:03' )
		HostD = self.addHost( 'hD' , mac = '00:00:00:00:00:04' )
		HostE = self.addHost( 'hE' , mac = '00:00:00:00:00:05' )
		HostF = self.addHost( 'hF' , mac = '00:00:00:00:00:06' )

		Servidor = self.addHost( 'hG' , mac = '00:00:00:00:00:07' )
		
		# Se aniaden los 6 switchs
		SwitchT = self.addSwitch( 's1', dpid="1" )
		SwitchU = self.addSwitch( 's2', dpid="2" )
		SwitchW = self.addSwitch( 's3', dpid="3" )
		SwitchY = self.addSwitch( 's4', dpid="4" )
		SwitchV = self.addSwitch( 's5', dpid="5" )
		SwitchX = self.addSwitch( 's6', dpid="6" )
		SwitchZ = self.addSwitch( 's7', dpid="7" )
		
		
		# conexiones entre host y switch
		self.addLink( HostA, SwitchV, 0, 1 )
		self.addLink( HostB, SwitchV, 0, 2 )
		
		self.addLink( HostC, SwitchX, 0, 3 )
		self.addLink( HostD, SwitchX, 0, 4 )
		
		self.addLink( HostE, SwitchZ, 0, 5 )
		self.addLink( HostF, SwitchZ, 0, 6 )

		self.addLink( Servidor, SwitchT, 16, 15 )
		
		# conexiones entre switches
		self.addLink( SwitchT, SwitchV, 17, 18 )
		self.addLink( SwitchV, SwitchX, 19, 20 )
		self.addLink( SwitchX, SwitchZ, 21, 22 )

		self.addLink( SwitchZ, SwitchY, 7, 8 )
		self.addLink( SwitchY, SwitchW, 9, 10 )
		self.addLink( SwitchW, SwitchU, 11, 12 )
		self.addLink( SwitchU, SwitchT, 13, 14 )

		self.addLink( SwitchV, SwitchU, 23, 24 )
		self.addLink( SwitchX, SwitchW, 25, 26 )


		

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ), 'Red1': (lambda: Red1() ), 'Red2': (lambda: Red2() ) }







