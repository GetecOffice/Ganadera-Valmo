"""SELECT Aplicacion_tblclientes.Nombre, Aplicacion_tblcorrales.Descripcion,
                SUM(case WHEN  Aplicacion_tblmovimientoanimales.IDMovimiento_id = 1 AND DATE(Aplicacion_tblmovimientoanimales.Fecha) 
                    BETWEEN DATE(Aplicacion_tblcorrales.FechaAsigna) AND %s THEN  Aplicacion_tbldetallemovanimales.Cantidad ELSE 0 END) - 
                SUM(case WHEN  Aplicacion_tblmovimientoanimales.IDMovimiento_id = 2 AND DATE(Aplicacion_tblmovimientoanimales.Fecha)  
                    BETWEEN DATE(Aplicacion_tblcorrales.FechaAsigna) AND %s THEN  Aplicacion_tbldetallemovanimales.Cantidad   ELSE 0 END) AS INICIAL,
                SUM(case WHEN  Aplicacion_tblmovimientoanimales.IDMovimiento_id = 1 AND DATE(Aplicacion_tblmovimientoanimales.Fecha) 
                    BETWEEN %s AND %s THEN  Aplicacion_tbldetallemovanimales.Cantidad ELSE 0 END) AS ENTRADA,
                SUM(case WHEN  Aplicacion_tblmovimientoanimales.IDMovimiento_id = 2 AND DATE(Aplicacion_tblmovimientoanimales.Fecha) 
                    BETWEEN %s AND %s THEN  Aplicacion_tbldetallemovanimales.Cantidad  ELSE 0 END) AS SALIDA
                FROM  Aplicacion_tblmovimientoanimales
                INNER JOIN Aplicacion_tblclientes ON Aplicacion_tblclientes.ID = Aplicacion_tblmovimientoanimales.IDCliente_id 
                INNER JOIN Aplicacion_tbldetallemovanimales ON  Aplicacion_tblmovimientoanimales.Folio = Aplicacion_tbldetallemovanimales.IDFolio
                INNER JOIN Aplicacion_tblcorrales ON  Aplicacion_tblcorrales.ID = Aplicacion_tbldetallemovanimales.IDCorral_id
                WHERE  Aplicacion_tbldetallemovanimales.IDCorral_id IN 
                    (SELECT  Aplicacion_tblcorrales.ID FROM Aplicacion_tblcorrales where  Aplicacion_tblcorrales.IDCliente_id = %s)
                                AND Aplicacion_tblmovimientoanimales.IDCliente_id = %s
                GROUP BY Aplicacion_tbldetallemovanimales.IDCorral_id, Aplicacion_tblclientes.Nombre """